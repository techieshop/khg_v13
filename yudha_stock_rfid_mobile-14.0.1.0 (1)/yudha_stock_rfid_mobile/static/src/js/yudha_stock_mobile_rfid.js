// Author   => Albertus Restiyanto Pramayudha
// email    => xabre0010@gmail.com
// linkedin => https://www.linkedin.com/in/albertus-restiyanto-pramayudha-470261a8/
// youtube  => https://www.youtube.com/channel/UCCtgLDIfqehJ1R8cohMeTXA

odoo.define('yudha_stock_rfid_mobile.stock.mobile_barcode', function (require) {
"use strict";

var linesWidget = require('yudha_stock_rfid.LinesWidget');
var RfidMainMenu = require('yudha_stock_rfid.MainMenu').MainMenu;

var config = require('web.config');
var core = require('web.core');

const mobile = require('web_mobile.core');

var _t = core._t;

function YudhaopenMobileScanner (callback) {
    mobile.methods.scanRfid().then(function (response) {
        var rfid = response.data;
        if (rfid){
            callback(rfid);
            mobile.methods.vibrate({'duration': 100});
        } else {
            mobile.methods.showToast({'message':_t('Please, Scan again !!')});
        }
    });
}
RfidMainMenu.include({
    events: _.defaults({
        'click .o_stock_mobile_rfid': 'yudha_open_mobile_scanner'
    }, RfidMainMenu.prototype.events),
    init: function () {
        this.mobileMethods = mobile.methods;
        return this._super.apply(this, arguments);
    },
    yudha_open_mobile_scanner: function() {
        var self = this;
        yudhaopenMobileScanner(function (rfid) {
            self._onrfidscanned(rfid);
        });
    }
});

linesWidget.include({
    events: _.defaults({
        'click .o_stock_mobile_barcode': '_onYudhaOpenMobileScanner',
    }, linesWidget.prototype.events),
    init: function () {
        this.mobileMethods = mobile.methods;
        return this._super.apply(this, arguments);
    },

    _scrollToLine: function ($body, $line) {
        if (config.device.isMobile) {
            $body = $('html, body');
            $body.animate({
                scrollTop: $line.position().top - $body.height() / 2 + $line.height() / 2
            }, 500);
        } else {
            this._super.apply(this, arguments);
        }
    },

    _onYudhaOpenMobileScanner: function () {
        YudhaopenMobileScanner(function (rfid) {
            core.bus.trigger("rfid_scanned", rfid);
    });
    },
});

});
