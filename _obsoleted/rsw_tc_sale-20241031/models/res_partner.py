# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    tc_picking_ids = fields.Many2many("stock.picking")
    past_sale_line_ids = fields.Char()

    def open_sale(self):
        return {
            'view_mode': 'form',
            'view_id': False,
            'view_type': 'form',
            'res_model': 'sale.order',
            'type': 'ir.actions.act_window',
            'context': {'default_partner_id': self.id}
        }

    def _compute_sale_line(self):
        for rec in self:
            sale_line_ids = []
            picking_ids = []
            sale_line = self.env['sale.order.line'].search(
                [('order_id', 'in', rec.sale_order_ids.ids), ('state', 'in', ('sale', 'done'))])
            for line in sale_line:
                if line.product_uom_qty != line.qty_delivered:
                    sale_line_ids.append(line.id)
                    picking_ids.extend(line.order_id.picking_ids.ids)
            if not rec.past_sale_line_ids:
                rec.past_sale_line_ids = sale_line_ids
                rec.tc_picking_ids = [(6, 0, picking_ids)]
            if eval(rec.past_sale_line_ids) != sale_line_ids:
                command = []
                a = set(eval(rec.past_sale_line_ids))
                b = set(sale_line_ids)
                removed_ids = list(a - b)
                added_ids = list(b - a)
                if added_ids:
                    add_picking_ids = self.env['stock.move'].search([('sale_line_id', 'in', added_ids)]).picking_id
                    command.extend([(4, i) for i in add_picking_ids.ids])
                if removed_ids:
                    rm_picking_ids = self.env['stock.move'].search([('sale_line_id', 'in', removed_ids)]).picking_id
                    command.extend([(3, i) for i in rm_picking_ids.ids])
                rec.tc_picking_ids = command
                rec.past_sale_line_ids = sale_line_ids
            rec.sale_order_line_ids = sale_line_ids

    def _compute_picking_ids(self):
        for rec in self:
            pick = 0
            for order in rec.sale_order_ids:
                pick += len(order.mapped('picking_ids'))
            rec.delivery_count = pick

    sale_order_line_ids = fields.Many2many('sale.order.line', compute='_compute_sale_line')
    delivery_count = fields.Integer(string='Delivery Orders', compute='_compute_picking_ids')

    def action_view_delivery(self):
        '''
        This function returns an action that display existing delivery orders
        of given sales order ids. It can either be a in a list or in a form
        view, if there is only one delivery order to show.
        '''
        action = self.env.ref('stock.action_picking_tree_all').read()[0]
        pickings = self.env['stock.picking']
        for order in self.sale_order_ids:
            pickings += order.mapped('picking_ids')
        if len(pickings) > 1:
            action['domain'] = [('id', 'in', pickings.ids)]
        elif pickings:
            form_view = [(self.env.ref('stock.view_picking_form').id, 'form')]
            if 'views' in action:
                action['views'] = form_view + [(state, view) for state, view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = pickings[0].id
        return action

    def open_transfer(self):
        operation_type = self.env['stock.picking.type'].search([('code', '=', 'outgoing')], limit=1)
        return {
            'view_mode': 'form',
            'view_id': False,
            'view_type': 'form',
            'res_model': 'stock.picking',
            'type': 'ir.actions.act_window',
            'context': {'default_partner_id': self.id, 'default_restaurant_department': 'kitchen',
                        'default_picking_type_id': operation_type.id, 'partner_transfer': True}
        }


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    qty_request = fields.Float()
    qty_remaining = fields.Float()

    @api.onchange('partner_id')
    def create_stock_move(self):
        if self.partner_id and self._context.get('partner_transfer'):
            product_line = self.env['sale.order.line'].read_group(
                [('id', 'in', self.partner_id.sale_order_line_ids.ids)], ['product_uom_qty', 'qty_delivered'],
                'product_id')
            # for line in self.partner_id.sale_order_line_ids:
            #     product_uom_qty = 0
            #     qty_delivered = 0
            #     sale_line = []
            #     data = {'product_uom_qty': line.product_uom_qty, 'qty_delivered': line.qty_delivered,
            #             'sale_line': sale_line}
            #     if product_line.get(line.product_id.id):
            #         product_line[line.product_id.id].get('product_uom_qty', 0)
            #         product_uom_qty = product_line.get(line.product_id.id).get('product_uom_qty')
            #         qty_delivered = product_line.get(line.product_id.id).get('qty_delivered')
            #         sale_line = product_line.get(line.product_id.id).get('sale_line')
            #     sale_line.append(line.id)
            #     product_line.update({line.product_id.id: {'product_uom_qty': line.product_uom_qty + product_uom_qty,
            #                                               'qty_delivered': line.qty_delivered + qty_delivered,
            #                                               'sale_line': sale_line}})
            move_ids = self.partner_id.tc_picking_ids.move_ids_without_package
            new_moves = []
            sale_ids = []
            for product_data in product_line:
                product_id = self.env['product.product'].browse(product_data['product_id'][0])
                # sale_line_id = self.env['sale.order.line'].browse(qty.get('sale_line'))
                # qty_request = 0
                # tc_stock_picking_id = []
                # for sale_line in sale_line_id:
                #     for picking in sale_line.tc_stock_picking_ids:
                #         if picking in tc_stock_picking_id:
                #             continue
                #         qty_request += sum(picking.move_ids_without_package.filtered(
                #             lambda x: x.product_id == product_id).mapped('qty_request'))
                #         sale_ids.append(sale_line.id)
                #         tc_stock_picking_id.append(picking.id)
                # qty_delivered = sum(sale_line_id.mapped("qty_delivered")) + qty_request
                qty_delivered = sum(move_ids.filtered(lambda x: x.product_id.id == product_id.id).mapped('quantity_done'))
                qty_remaining = product_data.get('product_uom_qty') - qty_delivered
                new_moves.append(
                    (0, 0,
                     {'name': '/', 'product_id': product_id.id, 'product_uom_qty': product_data.get('product_uom_qty'),
                      # 'qty_request': qty_remaining,
                      'qty_remaining': qty_remaining,
                      'product_uom': product_id.uom_id.id,
                      'location_id': self.location_id.id,
                      'description_picking': product_id._get_description(self.picking_type_id)}))
            self.move_ids_without_package = new_moves
            self.tc_sale_order_line = list(set(sale_ids))

    @api.model
    def create(self, vals):
        res = super(StockPicking, self).create(vals)
        res.partner_id.tc_picking_ids = [(4, res.id)]
        if self._context.get('partner_transfer') == True:
            sale_order_line = self.env['sale.order.line'].browse(eval(res.tc_sale_order_line))
            sale_order_line.tc_stock_picking_ids = [(6, 0, res.ids + sale_order_line.tc_stock_picking_ids.ids)]
        return res


class StockMove(models.Model):
    _inherit = 'stock.move'

    qty_request = fields.Float()
    qty_remaining = fields.Float()

    # @api.onchange('quantity_done')
    # def onchange_quantity_done(self):
    #     if self.quantity_done:
    #         self.qty_request = self.quantity_done
