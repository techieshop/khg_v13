# -*- coding: utf-8 -*-

import time
from odoo import api, fields, models, _
from datetime import datetime
import odoo.addons.decimal_precision as dp
from odoo.exceptions import UserError


class createpurchaseorder(models.TransientModel):
    _name = 'create.purchaseorder'
    _inherit = 'mail.thread'
    _description = "Create Purchase Order for Partner"

    def compute_partners(self):
        type_id = self.env.ref('rsw_contact.partner_type_internal_company', raise_if_not_found=False)
        return self.env['res.partner'].search([]).filtered(lambda m: type_id.id in m.newtype.ids).ids

    new_order_line_ids = fields.One2many('getsale.orderdata', 'new_order_line_id', String="Order Line")
    partner_id = fields.Many2one('res.partner', string='Vendor', required=True)
    date_order = fields.Datetime(string='Order Date', required=True, copy=False, default=fields.Datetime.now)

    partners = fields.Many2many(
        comodel_name='res.partner',
        default=compute_partners,
        string='Partners')

    @api.model
    def default_get(self, default_fields):
        res = super(createpurchaseorder, self).default_get(default_fields)
        data = self.env['sale.order'].browse(self._context.get('active_ids', []))
        update = []
        for record in data.order_line:
            update.append((0, 0, {
                'product_id': record.product_id.id,
                'product_uom': record.product_uom.id,
                'order_id': record.order_id.id,
                'name': record.name,
                'product_qty': record.product_uom_qty,
                'price_unit': record.price_unit,
                'product_subtotal': record.price_subtotal,
                'x_po_cartoon':record.x_so_cartoon,
                'x_product_standard_weight':record.x_product_standard_weight
            }))
        res.update({'partner_id': data.company_id.partner_id.id, 'new_order_line_ids': update})
        return res

    def action_create_purchase_order(self):
        self.ensure_one()
        res = self.env['purchase.order'].browse(self._context.get('id', []))
        value = []
        pricelist = self.partner_id.property_product_pricelist
        partner_pricelist = self.partner_id.property_product_pricelist
        sale_order_name = ""
        for data in self.new_order_line_ids:
            sale_order_name = data.order_id.name
            if partner_pricelist:
                product_context = dict(self.env.context, partner_id=self.partner_id.id, date=self.date_order,
                                       uom=data.product_uom.id)
                final_price, rule_id = partner_pricelist.with_context(product_context).get_product_price_rule(
                    data.product_id, data.product_qty or 1.0, self.partner_id)

            else:
                final_price = data.product_id.standard_price

            value.append([0, 0, {
                'product_id': data.product_id.id,
                'name': data.name,
                'product_qty': data.product_qty,
                'order_id': data.order_id.id,
                'product_uom': data.product_uom.id,
                'taxes_id': data.product_id.supplier_taxes_id.ids,
                'date_planned': data.date_planned,
                'price_unit': final_price,
                'x_po_cartoon':data.x_po_cartoon,
                'x_product_standard_weight':data.x_product_standard_weight
            }])
        picking_type = self.env['stock.picking.type'].sudo().search([('code','=','incoming'),('company_id','=',7)], limit=1)
        purchase_order = res.sudo().create({
            'partner_id': self.partner_id.id,
            'date_order': str(self.date_order),
            'order_line': value,
            'origin': sale_order_name,
            'partner_ref': sale_order_name,
            'company_id': 7,
            'picking_type_id': picking_type.id
        })
        sale_order = self.env['sale.order'].browse(self._context.get('active_ids', []))
        message = '<a href="#" data-oe-id=' + str(
            purchase_order.id) + ' data-oe-model="purchase.order">@' + purchase_order.name + '</a>'
        sale_order.message_post(body=message)
        return res


class Getsaleorderdata(models.TransientModel):
    _name = 'getsale.orderdata'
    _description = "Get Sale Order Data"

    new_order_line_id = fields.Many2one('create.purchaseorder')

    product_id = fields.Many2one('product.product', string="Product", required=True)
    name = fields.Char(string="Description")
    product_qty = fields.Float(string='Quantity', required=True)
    date_planned = fields.Datetime(string='Scheduled Date', default=datetime.today())
    product_uom = fields.Many2one('product.uom', string='Product Unit of Measure')
    order_id = fields.Many2one('sale.order', string='Order Reference', required=True, ondelete='cascade', index=True,
                               copy=False)
    price_unit = fields.Float(string='Unit Price', required=True, digits=dp.get_precision('Product Price'))
    product_subtotal = fields.Float(string="Sub Total", compute='_compute_total')
    x_po_cartoon = fields.Integer(string="Cartoon",default=1)
    x_product_standard_weight = fields.Float(string="Packing Spec (kg/pack)",default=10.8,digits = (12,4))

    @api.depends('product_qty', 'price_unit')
    def _compute_total(self):
        for record in self:
            record.product_subtotal = record.product_qty * record.price_unit
