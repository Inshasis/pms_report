# Copyright (c) 2024, Huda Infotech and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    conditions, filters = get_conditions(filters)
    columns = get_columns(filters)
    data = get_data(conditions, filters)

    return columns, data

def get_columns(filters):
    columns = [
        {"label": ("Property"), "fieldname": "property", "fieldtype": "Link", "options": "Asset", "width": 200},
        {"label": ("Tenant"), "fieldname": "tenant", "fieldtype": "Link", "options": "Customer", "width": 200},
        {"label": ("Lease Start Date"), "fieldname": "lease_start_date", "fieldtype": "Date", "width": 120},
        {"label": ("Lease End Date"), "fieldname": "lease_end_date", "fieldtype": "Date", "width": 120},
        {"label": ("Days Remaining"), "fieldname": "days_remaining", "fieldtype": "Int", "width": 100},
    ]
    return columns

def get_conditions(filters):
    conditions = ""

    if filters.get("from_date"):conditions += " AND p.start_date >= %(from_date)s"

    if filters.get("to_date"):conditions += " AND p.end_date <= %(to_date)s"

    return conditions,filters

def get_data(conditions,filters):
    data = frappe.db.sql("""
        SELECT
            p.asset as property,
            p.tenant as tenant,
            p.start_date as lease_start_date,
            p.end_date as lease_end_date,
            DATEDIFF(p.end_date, CURDATE()) as days_remaining
        FROM
            `tabTenancy` p
        WHERE
            p.docstatus = 1
            AND DATEDIFF(p.end_date, CURDATE()) <= 30
            {conditions}
    """.format(conditions=conditions), filters, as_dict=1)
    
    return data


