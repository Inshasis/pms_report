# Copyright (c) 2024, Huda Infotech and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    conditions, values = get_conditions(filters)
    columns = get_columns()
    data = get_data(conditions, values)

    return columns, data

def get_columns():
    columns = [
        {"fieldname": "asset_name", "label": "Asset Name", "fieldtype": "Data"},
        {"fieldname": "asset", "label": "Asset", "fieldtype": "Link", "options": "Asset"},
        {"fieldname": "tenant", "label": "Tenant", "fieldtype": "Link", "options": "Tenant"},
        {"fieldname": "landlord", "label": "Landlord", "fieldtype": "Link", "options": "Landlord"},
        {"fieldname": "contract", "label": "Contract", "fieldtype": "Link", "options": "Contract"},
        {"fieldname": "is_tenant_tenancy", "label": "Is Tenant Tenancy", "fieldtype": "Check"},
        {"fieldname": "is_landlord_tenancy", "label": "Is Landlord Tenancy", "fieldtype": "Check"},
        {"fieldname": "rent_type", "label": "Rent Type", "fieldtype": "Data"},
        {"fieldname": "ground_rent", "label": "Ground Rent", "fieldtype": "Currency"},
        {"fieldname": "advance_amount", "label": "Advance Amount", "fieldtype": "Currency"},
        {"fieldname": "number_of_rent_booked", "label": "Number of Rent Booked", "fieldtype": "Int"},
        {"fieldname": "total_rent_amount", "label": "Total Rent Amount", "fieldtype": "Currency"},
        {"fieldname": "invoice", "label": "Invoice", "fieldtype": "Link", "options": "Sales Invoice"},
        {"fieldname": "is_paid", "label": "Is Paid", "fieldtype": "Check"},
        {"fieldname": "payment_entry", "label": "Payment Entry", "fieldtype": "Link", "options": "Payment Entry"},
        {"fieldname": "company", "label": "Company", "fieldtype": "Link", "options": "Company"},
        {"fieldname": "start_date", "label": "Start Date", "fieldtype": "Date"},
        {"fieldname": "end_date", "label": "End Date", "fieldtype": "Date"},
    ]
    return columns

def get_conditions(filters):
    conditions = ""
    # if filters.get("start_date"):
    #     conditions += " AND t.start_date <= %(start_date)s"
    # if filters.get("end_date"):
    #     conditions += " AND t.end_date >= %(end_date)s"
    
    return conditions, filters

def get_data(conditions, values):
    data = frappe.db.sql(f"""
        SELECT
            t.asset as asset,
            t.asset_name as asset_name,
            t.tenant as tenant,
            t.landlord as landlord,
            t.custom_contract as contract,
            t.is_tenant_tenancy as is_tenant_tenancy,
            t.is_landlord_tenancy as is_landlord_tenancy,
            t.rent_type as rent_type,
            t.ground_rent as ground_rent,
            t.advance_deposit as advance_amount,
            t.number_of_deposit_booked as number_of_rent_booked,
            t.total_deposit_amount as total_rent_amount,
            t.invoice as invoice,
            t.is_paid as is_paid,
            t.payment_entry as payment_entry,
            t.company as company,
            t.start_date as start_date,
            t.end_date as end_date
        FROM
            `tabTenancy` t
        WHERE
            1=1 {conditions}
        ORDER BY
            t.name ASC
    """, values, as_dict=True)

    return data
