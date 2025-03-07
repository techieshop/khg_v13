odoo.define('rsw_possearch_serial.pos_search_by_serial', function (require) {
    "use strict";

    var pos = require('point_of_sale.models');
    var screens = require('point_of_sale.screens');

    // Extend the Product model to search by stock.move.line serial number
    pos.load_new_product = function (serialNumber) {
        var self = this;

        // Call the existing search method on stock.move.line
        this.rpc({
            model: 'stock.move.line',
            method: 'search_read',
            args: [[['lot_id.name', '=', serialNumber]], ['product_id', 'qty_done']],
        }).then(function (lines) {
            if (lines.length) {
                // Get the product ID from the first line found
                var productId = lines[0].product_id[0];
                
                // Add the product to the cart (you may need to adjust how you add the product)
                self.add_product(productId);
            } else {
                // Handle the case where no product is found
                alert('No product found with this serial number: ' + serialNumber);
            }
        });
    };

    // Override the barcode handler to call your new method
    screens.ProductScreenWidget.include({
        barcode_product: function (barcode) {
            var self = this;
            this.load_new_product(barcode);
        },
    });
});