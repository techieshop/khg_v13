# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import fields, models, tools


def deg_default_discount(unit_price_sold):
    return (unit_price_sold * 15) / 100


class CustomPurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def write(self, values):
        date_approve = values.get('date_approve')
        if date_approve:
            for rec in self:
                values['date_approve'] = rec.date_order
        return super(CustomPurchaseOrder, self).write(values)


class CustomPosOrderLine(models.Model):
    _inherit = "pos.order.line"

    session_id = fields.Many2one('pos.session', string='Session', related='order_id.session_id', store=True)
    currency_id = fields.Many2one('res.currency', related='session_id.currency_id', string="Currency", store=True)
    state = fields.Selection('Status', related='order_id.state', store=True)
    user_id = fields.Many2one(related='order_id.user_id', store=True)
    partner_id = fields.Many2one('res.partner', string='Customer', related='order_id.partner_id', store=True)
    date_order = fields.Datetime(string='Date', related='order_id.date_order', store=True)
    product_categ_id = fields.Many2one('product.category', string='Product Category', related='product_id.categ_id',
                                       store=True)
    purchase_state = fields.Boolean(string="Purchase", default=False)

    def action_auto_purchase(self):
        purchase_obj = self.env['purchase.order']
        active_ids = self.env.context.get('active_ids')
        browse_id = self.search([('id', 'in', active_ids)], order='date_order', limit=1)

        # get first day month from the smallest date

        date_end = fields.Datetime.from_string(browse_id.date_order)
        if date_end.day > 25:
            date_end += timedelta(7)
        date_order = fields.Datetime.to_string(date_end.replace(day=1, hour=0, minute=0, second=0, microsecond=0))

        # get all line not pruchased

        browse_pos_ids = self.browse(active_ids).filtered(lambda x: x.purchase_state is False)

        partner_id = self.env['res.partner'].search([('name', 'ilike', '泰昌肉食公司')], limit=1)
        if not partner_id:
            partner_id = self.env['res.partner'].search([], limit=1)

        if not browse_pos_ids:
            return
        purchase_id = purchase_obj.create({
            'partner_id': partner_id.id,
            'date_order': date_order,
        })
        product_ids = browse_pos_ids.mapped('product_id')
        for product_line in product_ids:
            same_line_ids = browse_pos_ids.filtered(lambda x: x.product_id == product_line and not x.purchase_state)
            sum_qty = sum(line.qty for line in same_line_ids)
            self.env['purchase.order.line'].create({
                'name': product_line.name,
                'product_id': product_line.id,
                'product_qty': sum_qty,
                'product_uom': product_line.uom_po_id.id,
                # 'taxes_id': [(6, 0, product_pos.tax_ids.ids)],
                'price_unit': same_line_ids[0].price_unit - deg_default_discount(same_line_ids[0].price_unit),
                'order_id': purchase_id.id,
                'date_planned': date_order,
            })
            for item in same_line_ids:
                item.write({
                    'purchase_state': True
                })
        return {
            'name': purchase_id.display_name,
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'purchase.order',
            'res_id': purchase_id.id,
            'target': 'target',
        }


class CustomPosOrderLineProduct(models.Model):
    _name = "pos.order.line.product"
    _auto = False

    product_id = fields.Many2one('product.product', string='Product')
    line_ids = fields.Char(string="Agregat line")
    qty = fields.Float('Quantity', digits='Product Unit of Measure')
    price_unit = fields.Float(string='Unit Price', digits=0)
    price_subtotal_incl = fields.Float(string='Subtotal', digits=0)
    date_order = fields.Datetime(string='Date')
    date_mont = fields.Datetime(string='Date Month')
    purchase_state = fields.Boolean(string="Purchase", default=False)
    product_categ_id = fields.Many2one('product.category', string='Product Category')
    currency_id = fields.Many2one('res.currency', string="Currency")

    def init(self):
        tools.drop_view_if_exists(self._cr, 'pos_order_line_product')
        self.env.cr.execute("""CREATE or REPLACE VIEW pos_order_line_product as (
           SELECT
                min(posl.id) as id,
                CAST(ARRAY_AGG(posl.id) AS VARCHAR) as line_ids,
                posl.product_id as product_id,
                posl.price_unit as price_unit,
                sum(posl.qty) as qty,
                sum(posl.price_subtotal_incl) as price_subtotal_incl,
                min(posl.date_order) as date_order,
                DATE_TRUNC('month',date_order) as date_mont,                
                posl.purchase_state as purchase_state,                
                posl.product_categ_id as product_categ_id,                
                posl.currency_id as currency_id                
           FROM pos_order_line posl
           GROUP BY product_id,purchase_state,price_unit,currency_id,product_categ_id,date_mont)""")

    def action_auto_purchase(self):
        purchase_obj = self.env['purchase.order']
        active_ids = self.env.context.get('active_ids')

        browse_id = self.search([('id', 'in', active_ids)], order='date_order', limit=1)

        # get first day month from the smallest date

        date_end = fields.Datetime.from_string(browse_id.date_order)
        if date_end.day > 25:
            date_end += timedelta(7)
        date_order = fields.Datetime.to_string(date_end.replace(day=1, hour=0, minute=0, second=0, microsecond=0))

        # get all line not pruchased

        browse_pos_ids = self.browse(active_ids).filtered(lambda x: x.purchase_state is False)

        partner_id = self.env['res.partner'].search([('name', 'ilike', '泰昌肉食公司')], limit=1)
        if not partner_id:
            partner_id = self.env['res.partner'].search([], limit=1)
        print(partner_id.name, partner_id.id)
        if not browse_pos_ids:
            return
        purchase_id = purchase_obj.create({
            'partner_id': partner_id.id,
            'date_order': date_order,
        })
        product_ids = browse_pos_ids.mapped('product_id')
        for product_line in product_ids:
            same_line_ids = browse_pos_ids.filtered(lambda x: x.product_id == product_line and not x.purchase_state)
            sum_qty = sum(line.qty for line in same_line_ids)
            self.env['purchase.order.line'].create({
                'name': product_line.name,
                'product_id': product_line.id,
                'product_qty': sum_qty,
                'product_uom': product_line.uom_po_id.id,
                # 'taxes_id': [(6, 0, product_pos.tax_ids.ids)],
                'price_unit': same_line_ids[0].price_unit - deg_default_discount(same_line_ids[0].price_unit),
                'order_id': purchase_id.id,
                'date_planned': date_order,
            })
            for item in same_line_ids:
                for pos_line_id in self.get_line(item.line_ids):
                    line_id = self.env['pos.order.line'].browse(int(pos_line_id))
                    line_id.write({
                        'purchase_state': True
                    })
        return {
            'name': purchase_id.display_name,
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'purchase.order',
            'res_id': purchase_id.id,
            'target': 'target',
        }

    def get_line(self, line_ids):
        line_ids = line_ids.strip('{')
        line_ids = line_ids.strip('}')
        return line_ids.split(',')
