odoo.define('rsw_pos_number.custom_pos_reference', function (require) {
    "use strict";
var models = require('point_of_sale.models');
var rpc = require('web.rpc');
var core = require('web.core');
var _t = core._t;
var _super_order = models.Order.prototype;
models.Order = models.Order.extend({
     initialize: function(attributes,options){
        var result = _super_order.initialize.apply(this,arguments);
        var self = result;
        rpc.query({
              model: 'pos.order',
              method: 'get_sequence',
              args: [1],
        }).then(function (result) {
            self.uid = result;
            self.name = self.uid;
        });
        return result;
    }
});
});