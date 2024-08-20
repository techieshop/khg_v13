odoo.define('rsw_custom_row_limit.ListView', function (require) {
    "use strict";

    var core = require('web.core');
    var ListView = require('web.ListView');

    var _t = core._t;

    ListView.include({
        init: function (viewInfo, params) {
            this._super.apply(this, arguments);
            
            // Origial Code
            // this.loadParams.limit = this.loadParams.limit || 80;
            
            // Override Code
            this.loadParams.limit = 400;

        },
    });
});