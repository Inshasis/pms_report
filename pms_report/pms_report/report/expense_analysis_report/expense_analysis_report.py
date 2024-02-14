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
		{"label": "Expense Account", "fieldname": "expense_account", "fieldtype": "Data"},
		{"label": "Total Amount", "fieldname": "total_amount", "fieldtype": "Currency", "options": "currency"},
		{"label": "Average Amount", "fieldname": "average_amount", "fieldtype": "Currency", "options": "currency"},
		{"label": "Number of Entries", "fieldname": "num_entries", "fieldtype": "Int"},
		{"label": "Maximum Amount", "fieldname": "max_amount", "fieldtype": "Currency", "options": "currency"},
		{"label": "Minimum Amount", "fieldname": "min_amount", "fieldtype": "Currency", "options": "currency"},
		{"label": "Standard Deviation", "fieldname": "std_deviation", "fieldtype": "Currency", "options": "currency"},
		{"label": "Variance", "fieldname": "variance", "fieldtype": "Currency", "options": "currency"},
		{"label": "Total Debit", "fieldname": "total_debit", "fieldtype": "Currency", "options": "currency"},
		{"label": "Total Credit", "fieldname": "total_credit", "fieldtype": "Currency", "options": "currency"},
		{"label": "Average Debit", "fieldname": "average_debit", "fieldtype": "Currency", "options": "currency"},
		{"label": "Average Credit", "fieldname": "average_credit", "fieldtype": "Currency", "options": "currency"}
	]
    return columns


def get_conditions(filters):
    conditions = ""
    # Add any additional conditions based on the filter parameters
    if filters.get("account"):
        conditions += " AND account = %(account)s"
    return conditions, filters


def get_data(conditions, filters):
    # Modify the query based on conditions and filters
    query = """
        SELECT
            account as expense_account,
            SUM(debit - credit) as total_amount,
            AVG(debit - credit) as average_amount,
            COUNT(name) as num_entries,
            MAX(debit - credit) as max_amount,
            MIN(debit - credit) as min_amount,
            STD(debit - credit) as std_deviation,
            VARIANCE(debit - credit) as variance,
            SUM(debit) as total_debit,
			SUM(credit) as total_credit,
			AVG(debit) as average_debit,
			AVG(credit) as average_credit
        FROM
            `tabGL Entry`
        WHERE
            docstatus = 1
            AND posting_date BETWEEN %(from_date)s AND %(to_date)s
            {conditions}
        GROUP BY
            account
    """.format(conditions=conditions)

    # Execute the query
    result = frappe.db.sql(query, {'from_date': filters.get("from_date"), 'to_date': filters.get("to_date"), 'account': filters.get("account")}, as_dict=True)

    return result
