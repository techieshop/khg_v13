from odoo import api, fields, models,  _
from odoo.exceptions import ValidationError


class SaleOrderSoldQtyReport(models.AbstractModel):
    _name = 'report.rsw_tc_sale_reports.report_sold_saleorder'

    def _get_report_values(self, docids, data=None):
        date = data['date']
        start_date = data['start_date']
        end_date = data['end_date']
        report_type = self.env.context['type_wizard']
        if report_type == 'shipment_handaing_report' or 'monthly_shipment_report':
            purchase_order_shipment = self.env['purchase.order.shipment'].search([
                ('date_order', '>=', start_date), ('date_order', '<=', end_date )
            ])
            if purchase_order_shipment:
                return {
                    'start_date' : start_date,
                    'end_date' : end_date,
                    'docs': purchase_order_shipment
                    }
            else:
                raise ValidationError(_("No Shipment."))
            
        if report_type == 'sold_product_report':
            sql_query = """
                    SELECT rp.name as customer_name, sol.name as product_name , 
                    sol.order_id as sale_order_id, so.name as ordername, 
                    sol.product_uom_qty as puchasedqty, sm.date as done_date,
                    sol.qty_delivered, sol.product_uom, sl.complete_name as location,
                    sol.price_unit as unit_price, pl.name as lot_name
                    FROM sale_order_line AS sol 
                    INNER join sale_order AS so ON sol.order_id = so.id
                    INNER join res_partner AS rp ON rp.id = so.partner_id
                    INNER join stock_move AS sm ON sm.sale_line_id = sol.id
                    INNER join product_product AS pp ON pp.id = sol.product_id
                    INNER join stock_move_line AS sml ON sml.move_id = sm.id
                    LEFT Join stock_production_lot AS pl ON pl.id = sml.lot_id
                    INNER join stock_location AS sl ON sl.id = sm.location_id 
                    WHERE
                    sml.date::timestamp::date = %s::timestamp::date;"""
            print("SQL QUERy", sql_query)
            self.env.cr.execute(sql_query, [date])
            query_results_drafts = self.env.cr.dictfetchall()
            if query_results_drafts:
                return {
                    'date' : date,
                    'data': query_results_drafts,
                    'doc_ids': docids
                }
            else:
                raise ValidationError(_("No Product Delivered on this Day."))


