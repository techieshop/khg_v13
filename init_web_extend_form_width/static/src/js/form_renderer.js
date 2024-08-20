odoo.define('init_web_extend_form_width.FormRenderer', function (require) {
    "use strict";
    var config = require('web.config');
    var FormRenderer = require('web.FormRenderer');
    FormRenderer.include({
        _renderTagSheet: function (node) {
            var context = this.state['context'];
            if (context['init_default']) {
                return this._super.apply(this, arguments);
            }
            this.has_sheet = true;
            if (!config.device.isMobile) {
                 var $sheet = $('<div>', {class: 'clearfix position-relative o_form_sheet init_web_extend_form'});
            }
            else {
                var $sheet = $('<div>', {class: 'clearfix position-relative o_form_sheet'});
            }
            $sheet.append(node.children.map(this._renderNode.bind(this)));
            return $sheet;
        },
    });

});
