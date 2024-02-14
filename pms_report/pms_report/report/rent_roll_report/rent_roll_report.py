# Copyright (c) 2024, Huda Infotech and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    conditions, filters = get_conditions(filters)
    columns = get_columns(filters)
    data = get_data(conditions, filters)

    return columns, data

def get_columns(filters):
    columns = [
		{"label": "Property", "fieldname": "property", "fieldtype": "Data"},
		{"label": "Tenant", "fieldname": "tenant", "fieldtype": "Data"},
		{"label": "Lease Start Date", "fieldname": "lease_start_date", "fieldtype": "Date"},
		{"label": "Lease End Date", "fieldname": "lease_end_date", "fieldtype": "Date"},
		{"label": "Rental Rate", "fieldname": "rental_rate", "fieldtype": "Currency", "options": "currency"},
		{"label": "Outstanding Balance", "fieldname": "outstanding_balance", "fieldtype": "Currency", "options": "currency"}
	]
    return columns

def get_conditions(filters):
    conditions = ""
    if filters.get("tenant"):
        conditions += " AND p.tenant = %(tenant)s"

    if filters.get("property"):
        conditions += " AND p.asset = %(property)s"
    
    return conditions, filters

def get_data(conditions, filters):
    data = frappe.db.sql("""
        SELECT
            p.asset as property,
            p.tenant as tenant,
            p.start_date as lease_start_date,
            p.end_date as lease_end_date,
            p.ground_rent as rental_rate,
            SUM(pe.pending_amount) as outstanding_balance
        FROM
            `tabTenancy` p
        LEFT JOIN
            `tabTenant Schedule` pe ON pe.parent = p.name
        WHERE
            p.docstatus = 1
            {conditions}
        GROUP BY
            p.asset, p.tenant, p.start_date, p.end_date, p.ground_rent
    """.format(conditions=conditions), filters, as_dict=1)

    return data