# -*- coding: utf-8 -*-

import time
from odoo import api, fields, models, _
from datetime import datetime
import odoo.addons.decimal_precision as dp
from odoo.exceptions import UserError


class createsaleorder(models.TransientModel):
    _name = "create.saleorder"
    _description = "Create Internal Sale Order"

    new_order_line_ids = fields.One2many(
        "getpurchase.orderdata", "new_order_line_id", String="Order Line"
    )

    # partner_id = fields.Many2one(
    #     "res.partner", string="Customer", required=True,default=12
    # )
    partner_id = fields.Many2one(
        "res.partner", string="Customer", required=True,default=36
    )
    date_order = fields.Datetime(
        string="Order Date", required=True, default=fields.Datetime.now
    )
    currency_id = fields.Many2one('res.currency', 'Currency', required=True, 
        default=lambda self: self.env.company.currency_id.id)
    origin_po = fields.Char('From Purchase')
    # @api.model
    # def default_get(self,  default_fields):
    # 	res = super(createsaleorder, self).default_get(default_fields)
    # 	record = self.env['purchase.order'].browse(self._context.get('active_ids',[]))
    # 	update = []
    # 	for record in record.order_line:
    # 		product = self.env['product.product'].browse(record.product_id)
    # 		unit_price = product.list_price
    # 		update.append((0,0,{
    # 				'product_id' : record.product_id.id,
    # 				'name' : record.name,
    # 				'product_qty' : record.product_qty,
    # 				'price_unit' : unit_price,
    # 				'product_subtotal' : record.price_subtotal,
    # 				'date_planned' : datetime.today(),
    # 			}))

    # 		res.update({'new_order_line_ids':update})
    # 	return res

    @api.model
    def default_get(self, default_fields):
        res = super(createsaleorder, self).default_get(default_fields)
        record = self.env["purchase.order"].browse(self._context.get("active_ids", []))
        record_currency=record.currency_id
        record_name=record.name
        update = []
        for record in record.order_line:
            product = record.product_id.with_context(pricelist=6)
            price_unit= record.price_unit 
            # qty_received=record.qty_received
            qty=record.product_qty
            if record.product_uom.id != product.uom_id.id:
                price_unit= (price_unit *  product.uom_id.factor_inv)
                # qty_received= qty_received * product.uom_id.factor_inv
                qty= qty / product.uom_id.factor_inv
            price_unit= price_unit * 1.055
            update.append(
                (
                    0,
                    0,
                    {
                        "product_id": record.product_id.id,
                        "name": record.name,
                        "x_so_cartoon": record.x_po_cartoon,
                        "x_product_standard_weight": record.x_product_standard_weight,
                        "product_qty": qty,
                        "price_unit": price_unit,
                        "product_subtotal": qty * price_unit,
                        "date_planned": datetime.today(),
                        "product_uom":product.uom_id.id,
                        "currency_id": record_currency.id
                    },
                )
            )

            res.update({"new_order_line_ids": update,})
        res.update({"currency_id": record_currency.id,"origin_po":record_name})
        return res

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            currency_id=self.partner_id.property_product_pricelist.currency_id.id
            if currency_id != self.currency_id.id:
                for record in self.new_order_line_ids:
                    record_price_unit= ( record.price_unit * self.currency_id.rate ) * self.partner_id.property_product_pricelist.currency_id.rate
                    record.write({
                        "currency_id": currency_id,
                        "price_unit" :record_price_unit
                    })
                self.write({'currency_id':currency_id})
    

    def action_create_sale_order(self):
        self.ensure_one()
        po = self.env["purchase.order"].browse(self._context.get("active_ids", []))
        res = self.env["sale.order"].browse(self._context.get("id", []))
        value = []
        for data in self.new_order_line_ids:
            value.append(
                [
                    0,
                    0,
                    {
                        "product_id": data.product_id.id,
                        "name": data.name,
                        "x_so_cartoon": data.x_so_cartoon,
                        "x_product_standard_weight": data.x_product_standard_weight,
                        "product_uom_qty": data.product_qty,
                        "price_unit": data.price_unit,
                        "product_uom":data.product_uom.id,
                        "currency_id": data.currency_id.id
                    },
                ]
            )
        sale = res.create({
                "partner_id": self.partner_id.id,
                "date_order": self.date_order,
                "order_line": value,
                "currency_id": self.currency_id.id,
                "origin_po":self.origin_po,
                "created_from_po":True
            })
        if sale:
            po.sale_order_id = sale.id
        return


class getpurchaseorder(models.TransientModel):
    _name = "getpurchase.orderdata"
    _description = "Get purchase Order Data"

    new_order_line_id = fields.Many2one("create.saleorder")
    currency_id = fields.Many2one('res.currency', 'Currency', required=True, 
        default=lambda self: self.env.company.currency_id.id)
    product_id = fields.Many2one("product.product", string="Product", required=True)
    name = fields.Char(string="Description", required=True)
    product_qty = fields.Float(string="Quantity", required=True)
    price_unit = fields.Float(string="Unit Price", required=True)
    product_subtotal = fields.Monetary(string="Sub Total", compute="_compute_total")
    date_planned = fields.Datetime(string="Receipt Date")
    x_so_cartoon = fields.Integer(string="Cartoon", default=1)
    product_uom = fields.Many2one('uom.uom', string='Product Unit of Measure')
    x_product_standard_weight = fields.Float(
        string="Packing Spec (kg/pack)", default=10.8,digits = (12,4)
    )

    @api.depends("product_qty", "price_unit")
    def _compute_total(self):
        for record in self:
            record.product_subtotal = record.product_qty * record.price_unit


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    sale_order_id = fields.Many2one("sale.order", string="Sale Order")
