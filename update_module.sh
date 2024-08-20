#!/bin/bash -v

odoobin=/usr/bin/odoo
odooconf=/etc/odoo/odoo.conf
echo $odoo_path

systemctl stop odoo13
#
# basic
#
$odoobin -c $odooconf -d $1 -u rsw_contact --stop-after-init
$odoobin -c $odooconf -d $1 -u res_partner_extended --stop-after-init
#$odoobin -c $odooconf -d $1 -u rsw_contacts_visibiality --stop-after-init
$odoobin -c $odooconf -d $1 -u rsw_custom_header_footer --stop-after-init
#$odoobin -c $odooconf -d $1 -u rsw_qweb_custom_header_footer --stop-after-init
#$odoobin -c $odooconf -d $1 -u rsw_internal_sku --stop-after-init
#
# accounting
#
#$odoobin -c $odooconf -d $1 -u rsw_accounting_reports_custom --stop-after-init
#$odoobin -c $odooconf -d $1 -u rsw_accounting_reports_layout --stop-after-init
#$odoobin -c $odooconf -d $1 -u rsw_account_report_extended --stop-after-init
#$odoobin -c $odooconf -d $1 -u rsw_custom_balance_sheet --stop-after-init
#$odoobin -c $odooconf -d $1 -u rsw_custom_pl_and_bs --stop-after-init
#$odoobin -c $odooconf -d $1 -u rsw_custom_profit_loss --stop-after-init
#$odoobin -c $odooconf -d $1 -u rsw_custom_trial_balance --stop-after-init
#$odoobin -c $odooconf -d $1 -u rsw_journal_number --stop-after-init
#$odoobin -c $odooconf -d $1 -u rsw_print_journal_entries --stop-after-init
#
# tc_sale
#
$odoobin -c $odooconf -d $1 -u rsw_tc_sale --stop-after-init
$odoobin -c $odooconf -d $1 -u rsw_tc_sale_reports --stop-after-init
$odoobin -c $odooconf -d $1 -u rsw_user_pricelist --stop-after-init
$odoobin -c $odooconf -d $1 -u rsw_so_create_product_1 --stop-after-init
#$odoobin -c $odooconf -d $1 -u rsw_sales_enhancement --stop-after-init
$odoobin -c $odooconf -d $1 -u rsw_sold_product_qty_report --stop-after-init
#
# delivery
#
$odoobin -c $odooconf -d $1 -u rsw_delivery_note --stop-after-init
$odoobin -c $odooconf -d $1 -u rsw_delivery_report --stop-after-init
$odoobin -c $odooconf -d $1 -u rsw_auto_refreshing --stop-after-init
#
# purchasing
#
$odoobin -c $odooconf -d $1 -u rsw_shipment_management --stop-after-init
$odoobin -c $odooconf -d $1 -u rsw_shipment_report --stop-after-init
$odoobin -c $odooconf -d $1 -u rsw_create_purchase_from_sales --stop-after-init
$odoobin -c $odooconf -d $1 -u rsw_convert_sales_from_purchase --stop-after-init
#
# inventory
#
$odoobin -c $odooconf -d $1 -u rsw_warehouse_report_app --stop-after-init
#$odoobin -c $odooconf -d $1 -u rsw_stock_report --stop-after-init
#$odoobin -c $odooconf -d $1 -u rsw_lots_enhancement --stop-after-init
#
# POS
#
$odoobin -c $odooconf -d $1 -u rsw_pos_category --stop-after-init
$odoobin -c $odooconf -d $1 -u rsw_pos_number --stop-after-init
$odoobin -c $odooconf -d $1 -u rsw_pos_purchase --stop-after-init
#
# Misc
#
#$odoobin -c $odooconf -d $1 -u rsw_khg_product --stop-after-init
#$odoobin -c $odooconf -d $1 -u rsw_kh_wholesale --stop-after-init
#
systemctl start odoo13
