import pg8000

# Configuration
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "KHG2022_0316"
DB_USER = "postgres"
DB_PASSWORD = "T0geth@r"

MODULES_TO_REMOVE = [
    "rsw_contact",
    "rsw_delivery_note",
    "rsw_delivery_report",
    "rsw_kh_delivery",
    "rsw_kh_core",
    "rsw_khg_core",
    "rsw_khg_product",
    "rsw_khg_purchase",
    "rsw_khg_sale",
    "rsw_tc_sale",
    "rsw_tc_sale_reports",
    "rsw_shipment_report",
    "rsw_shipment_management",
    "rsw_allow_add_lot",
    "rsw_auto_refreshing",
    "rsw_custom_header_footer",
    "rsw_custom_row_limit",
    "rsw_st_purchase",
    "rsw_so_create_product_1",
    "rsw_user_pricelist",
]

def connect_to_db():
    """Establish database connection using pg8000"""
    try:
        conn = pg8000.connect(
            host=DB_HOST,
            port=int(DB_PORT),
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print("✓ Successfully connected to database")
        return conn
    except Exception as e:
        print(f"✗ Connection failed: {sanitize_error(e)}")
        return None

def sanitize_error(error):
    """Handle encoding errors in error messages"""
    return str(error).encode('utf-8', errors='replace').decode('utf-8')

def remove_module_from_db(conn, module_name):
    """Completely remove a module and all related data"""
    try:
        cursor = conn.cursor()
        print(f"\nStarting removal of [{module_name}]")

        # 1. Remove attachments linked to module models
        cursor.execute("""
            DELETE FROM ir_attachment 
            WHERE res_model IN (
                SELECT model FROM ir_model WHERE module = %s
            )
        """, (module_name,))
        print(f"  → Removed {cursor.rowcount} attachments")

        # 2. Remove constraints
        cursor.execute("DELETE FROM ir_model_constraint WHERE module = %s", (module_name,))
        print(f"  → Removed {cursor.rowcount} constraints")

        # 3. Remove model relations
        cursor.execute("DELETE FROM ir_model_relation WHERE module = %s", (module_name,))
        print(f"  → Removed {cursor.rowcount} model relations")

        # 4. Remove models
        cursor.execute("DELETE FROM ir_model WHERE module = %s", (module_name,))
        print(f"  → Removed {cursor.rowcount} models")

        # 5. Remove model data
        cursor.execute("DELETE FROM ir_model_data WHERE module = %s", (module_name,))
        print(f"  → Removed {cursor.rowcount} model data entries")

        # 6. Remove views
        cursor.execute("""
            DELETE FROM ir_ui_view 
            WHERE id IN (
                SELECT res_id FROM ir_model_data 
                WHERE module = %s AND model = 'ir.ui.view'
            )
        """, (module_name,))
        print(f"  → Removed {cursor.rowcount} views")

        # 7. Remove menus
        cursor.execute("""
            DELETE FROM ir_ui_menu 
            WHERE id IN (
                SELECT res_id FROM ir_model_data 
                WHERE module = %s AND model = 'ir.ui.menu'
            )
        """, (module_name,))
        print(f"  → Removed {cursor.rowcount} menus")

        # 8. Remove security rules
        cursor.execute("""
            DELETE FROM ir_rule 
            WHERE id IN (
                SELECT res_id FROM ir_model_data 
                WHERE module = %s AND model = 'ir.rule'
            )
        """, (module_name,))
        print(f"  → Removed {cursor.rowcount} security rules")

        # 9. Remove access rights
        cursor.execute("""
            DELETE FROM ir_model_access 
            WHERE id IN (
                SELECT res_id FROM ir_model_data 
                WHERE module = %s AND model = 'ir.model.access'
            )
        """, (module_name,))
        print(f"  → Removed {cursor.rowcount} access rights")

        # 10. Remove the module itself
        cursor.execute("DELETE FROM ir_module_module WHERE name = %s", (module_name,))
        print(f"  → Removed module registry entry")

        conn.commit()
        cursor.close()
        print(f"✓ Successfully completed removal of [{module_name}]")

    except Exception as e:
        print(f"✗ Error removing {module_name}: {sanitize_error(e)}")
        conn.rollback()

def main():
    """Main execution flow"""
    conn = connect_to_db()
    if not conn:
        return

    try:
        print(f"\nStarting removal of {len(MODULES_TO_REMOVE)} modules")
        for index, module in enumerate(MODULES_TO_REMOVE, 1):
            print(f"\nModule {index}/{len(MODULES_TO_REMOVE)}")
            remove_module_from_db(conn, module)
        
        print("\n All modules removed successfully")

    except Exception as e:
        print(f"\n Critical error: {sanitize_error(e)}")
        conn.rollback()

    finally:
        conn.close()
        print("\nDatabase connection closed")

if __name__ == "__main__":
    main()