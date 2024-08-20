import pytz
from odoo import api, fields, models
from dateutil.relativedelta import relativedelta


class PosDetails(models.TransientModel):
    _inherit = 'pos.details.wizard'

    def _default_start_date(self):
        now = fields.Datetime.now().replace(hour=0, minute=0, second=0)
        now_tz = now.astimezone(pytz.timezone(self.env.user.tz)).replace(tzinfo=None)
        return now - relativedelta(hours=now_tz.hour)

    start_date = fields.Datetime(required=True, default=_default_start_date)

