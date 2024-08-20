from odoo import api, fields, models


class PosOrder(models.Model):
    _inherit = "pos.order"

    def get_sequence(self):
        po_env = self.env["pos.order"]
        sequence_number = 1
        current_date = fields.datetime.now()
        start_date = current_date.replace(hour=0, minute=0, second=0)
        end_date = current_date.replace(hour=23, minute=59, second=59)
        orders = po_env.search(
            [
                ("date_order", ">=", start_date),
                ("date_order", "<=", end_date),
            ]
        )
        order_ref_list = orders.filtered(lambda x: x.pos_reference and len(x.pos_reference) >= 4).mapped("pos_reference")
        order_ref_list = list(map(lambda x: int(x[-4:]), order_ref_list))
        if order_ref_list:
            sequence_number = max(order_ref_list) + 1
        return f"{current_date.strftime('%y%m%d')}{str(sequence_number).zfill(4)}"
