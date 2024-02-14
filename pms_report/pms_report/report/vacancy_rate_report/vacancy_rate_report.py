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
        {"label": ("Property"), "fieldname": "property", "fieldtype": "Link", "options": "Asset", "width": 200},
        {"label": ("Status"), "fieldname": "property_status", "fieldtype": "Data", "width": 120},
        {"label": ("Vacancy Start Date"), "fieldname": "start_date", "fieldtype": "Date", "width": 120},
        {"label": ("Vacancy End Date"), "fieldname": "end_date", "fieldtype": "Date", "width": 120},
        {"label": ("Vacancy Duration (Days)"), "fieldname": "vacancy_duration_days", "fieldtype": "Int", "width": 120},
    ]
    return columns

def get_conditions(filters):
    conditions = ""
    if filters.get("from_date"): conditions += " AND p.start_date >= %(from_date)s"
    if filters.get("to_date"): conditions += " AND p.end_date <= %(to_date)s"
    
    return conditions, filters

def get_data(conditions, filters):
    data = frappe.db.sql("""
        SELECT
            a.name as property, 
            a.property_status, 
            p.start_date,
            p.end_date, 
            DATEDIFF(p.end_date, p.start_date) as vacancy_duration_days
        FROM
            `tabAsset` a
        LEFT JOIN
            `tabTenancy` p ON p.asset = a.name
        WHERE
            p.docstatus = 1
            AND a.property_status = "Available"
            {conditions}
        GROUP BY
            a.name
    """.format(conditions=conditions), filters, as_dict=1)

    return data