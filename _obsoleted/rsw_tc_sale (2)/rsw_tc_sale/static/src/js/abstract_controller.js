odoo.define('rsw_tc_sale.AbstractControllerOpen', function (require) {
"use strict";

var KanbanRecord = require('web.KanbanRecord');

KanbanRecord.include({
    _onGlobalClick: function(event) {
        debugger;
        if (event.currentTarget.classList.value.split(' ').includes('open_sale')) {
            this.do_action({
                name: ('Attachments'),
                type: 'ir.actions.act_window',
                res_model: 'sale.order',
                views: [[false, 'form']],
                target: 'current',
                context: {
                    default_partner_id : this.recordData.id,
                    default_create_product : true,
                },
            });
        }
        else {
            this._super.apply(this, arguments);
        }
    },
});
})