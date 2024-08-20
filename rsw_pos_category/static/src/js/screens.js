odoo.define('rsw_pos_category.screens', function (require) {
    "use strict";

    var screens = require('point_of_sale.screens');

    screens.ProductCategoriesWidget.include({
        set_category : function(category){
            var db = this.pos.db;
            if(!category){
                this.category = db.get_category_by_id(db.root_category_id);
            }else{
                this.category = category;
            }
            this.breadcrumb = [];
            var ancestors_ids = db.get_category_ancestors_ids(this.category.id);
            for(var i = 1; i < ancestors_ids.length; i++){
                this.breadcrumb.push(db.get_category_by_id(ancestors_ids[i]));
            }
            if(this.category.id !== db.root_category_id){
                this.breadcrumb.push(this.category);
            }

            if(this.category.id === 0){
                this.subcategories = db.get_category_by_id(db.get_category_childs_ids(this.category.id));
            }else if(this.category.child_id.length === 0){
                this.subcategories = db.get_category_by_id(db.get_category_childs_ids(this.category.parent_id[0]));
            }else {
                this.subcategories = db.get_category_by_id(db.get_category_childs_ids(this.category.id));
            }
        },
    });
});
