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
        {"label": "Invoice", "fieldname": "invoice", "fieldtype": "Link", "options": "Sales Invoice"},
        {"label": "Invoice Date", "fieldname": "invoice_date", "fieldtype": "Date"},
        {"label": "Tenant", "fieldname": "customer", "fieldtype": "Link", "options": "Customer"},
        {"label": "Property", "fieldname": "property", "fieldtype": "Link","options":"Item"},
        {"label": "Rent Amount", "fieldname": "rent_amount", "fieldtype": "Currency"},
        {"label": "Payment Entry", "fieldname": "payment_entry", "fieldtype": "Link", "options": "Payment Entry"},
        {"label": "Payment Date", "fieldname": "payment_date", "fieldtype": "Date"},
        {"label": "Paid Amount", "fieldname": "paid_amount", "fieldtype": "Currency"},
        {"label": "Outstanding Amount", "fieldname": "outstanding_amount", "fieldtype": "Currency"},
        {"label": "Payment Status", "fieldname": "payment_status", "fieldtype": "Data"}
        # Add more columns as needed
    ]
    return columns



def get_conditions(filters):
    conditions = ""
    if filters.get("tenant"):
        conditions += " AND si.customer = %(tenant)s"

    if filters.get("property"):
        conditions += " AND sii.item_code = %(property)s"
    return conditions, filters
    

def get_data(conditions, filters):
    data = frappe.db.sql("""
        SELECT
            si.name as invoice,
            si.posting_date as invoice_date,
            si.customer as customer,
            si.grand_total as rent_amount,
            sii.item_code as property,
            pe.name as payment_entry,
            pe.posting_date as payment_date,
            pe.paid_amount as paid_amount,
            si.grand_total - COALESCE(pe.paid_amount, 0) as outstanding_amount,
            CASE
                WHEN pe.name IS NULL THEN 'Unpaid'
                WHEN pe.paid_amount < si.grand_total THEN 'Partially Paid'
                WHEN pe.paid_amount >= si.grand_total THEN 'Paid'
                ELSE 'Unpaid'
            END as payment_status
        FROM
            `tabSales Invoice` si
        LEFT JOIN
            `tabSales Invoice Item` sii ON sii.parent = si.name
        LEFT JOIN
            `tabPayment Entry Reference` per ON si.name = per.reference_name
        LEFT JOIN
            `tabPayment Entry` pe ON per.parent = pe.name
        WHERE
            si.docstatus = 1
            AND (pe.docstatus = 1 OR pe.docstatus IS NULL)
            {conditions}
    """.format(conditions=conditions), filters, as_dict=1)

    return data

# AND si.is_rent_invoice = 1 ///si.property as property,