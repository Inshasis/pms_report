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
        {"label": _("Property"), "fieldname": "property", "fieldtype": "Link", "options": "Asset", "width": 200},
        {"label": _("Tenant"), "fieldname": "tenant", "fieldtype": "Data", "width": 200},
        {"label": _("Move-in Date"), "fieldname": "start_date", "fieldtype": "Date", "width": 120},
        {"label": _("Move-out Date"), "fieldname": "end_date", "fieldtype": "Date", "width": 120},
        {"label": _("Turnover Duration (Days)"), "fieldname": "turnover_duration_days", "fieldtype": "Int", "width": 120},
        {"label": _("Rent Amount"), "fieldname": "rent_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Deposit Amount"), "fieldname": "deposit_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Total Invoice Amount"), "fieldname": "total_invoice_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Maintenance Cost"), "fieldname": "maintenance_cost", "fieldtype": "Currency", "width": 120},
        {"label": _("Insurance Cost"), "fieldname": "insurance_cost", "fieldtype": "Currency", "width": 120},
        {"label": _("Other Expenses"), "fieldname": "other_expenses", "fieldtype": "Currency", "width": 120},
        {"label": _("Net Profit"), "fieldname": "net_profit", "fieldtype": "Currency", "width": 120},
    ]
    return columns

def get_conditions(filters):
    conditions = ""

    if filters.get("from_date"): conditions += " AND p.start_date >= %(from_date)s"
    if filters.get("to_date"): conditions += " AND p.end_date <= %(to_date)s"
    if filters.get("tenant"): conditions += " AND t.tenant <= %(tenant)s"
    
    return conditions, filters

def get_data(conditions,filters):
    data = frappe.db.sql("""
        SELECT
            p.name as property,
            t.tenant as tenant,
            p.start_date,
            p.end_date,
            DATEDIFF(p.start_date, p.end_date) as turnover_duration_days,
            t.ground_rent,
            t.advance_deposit,
            t.total_deposit_amount
        FROM
            `tabAsset` p
        LEFT JOIN
            `tabTenancy` t ON p.name = t.asset
        WHERE
            p.docstatus = 1
            AND p.start_date IS NOT NULL
            AND p.end_date IS NOT NULL
            {conditions}
    """.format(conditions=conditions), filters, as_dict=1)

    return data
