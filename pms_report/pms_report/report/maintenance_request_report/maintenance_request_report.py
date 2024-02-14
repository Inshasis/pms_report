# Copyright (c) 2024, Huda Infotech and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    conditions, values = get_conditions(filters)
    columns = get_columns(filters)
    data = get_data(conditions, values)

    return columns, data

def get_columns(filters):
    columns = [
        {"fieldname": "name", "label": "Maintenance Request ID", "fieldtype": "Link", "options": "Maintenance Request", "width": 150},
        {"fieldname": "subject", "label": "Subject", "fieldtype": "Data", "width": 200},
        {"fieldname": "property", "label": "Property", "fieldtype": "Data","width": 150},
        {"fieldname": "priority", "label": "Priority", "fieldtype": "Select", "options": "Low\nMedium\nHigh", "width": 100},
        {"fieldname": "customer", "label": "Customer", "fieldtype": "Link", "options": "Customer", "width": 150},
        {"fieldname": "issue_type", "label": "Issue Type", "fieldtype": "Data", "width": 150},
        {"fieldname": "first_responded_on", "label": "First Responded On", "fieldtype": "Datetime", "width": 150},
        {"fieldname": "description", "label": "Description", "fieldtype": "Text", "width": 200},
        {"fieldname": "resolution_details", "label": "Resolution Details", "fieldtype": "Text", "width": 200},
        {"fieldname": "status", "label": "Status", "fieldtype": "Select", "options": "Open\nClosed", "width": 100},
        {"fieldname": "opening_date", "label": "Opening Date", "fieldtype": "Date", "width": 100},
        {"fieldname": "opening_time", "label": "Opening Time", "fieldtype": "Time", "width": 100}
        # Add more columns as needed
    ]
    return columns

def get_conditions(filters):
    conditions = ""
    values = {}

    if filters.get("from_date"):
        conditions += " AND opening_date >= %(from_date)s"
        values["from_date"] = filters["from_date"]

    if filters.get("to_date"):
        conditions += " AND opening_date <= %(to_date)s"
        values["to_date"] = filters["to_date"]

    if filters.get("maintenance_type"):
        conditions += " AND issue_type = %(maintenance_type)s"
        values["maintenance_type"] = filters["maintenance_type"]

    return conditions, values

def get_data(conditions, values):
    data = frappe.db.sql("""
        SELECT
            name,
            subject,
            property,
            priority,
            customer,
            issue_type,
            first_responded_on,
            description,
            resolution_details,
            status,
            opening_date,
            opening_time
        FROM
            `tabMaintenance Request`
        WHERE
            1=1 {conditions}
    """.format(conditions=conditions), values, as_dict=True)

    return data
