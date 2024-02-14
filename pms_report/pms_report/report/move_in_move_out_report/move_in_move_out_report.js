// Copyright (c) 2024, Huda Infotech and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Move-in Move-out Report"] = {
	"filters": [
		{
            "fieldname": "from_date",
            "label": __("From Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
            "reqd": 1
        },
        {
            "fieldname": "to_date",
            "label": __("To Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.get_today(),
            "reqd": 1
        },
        {
            "fieldname": "tenant",
            "label": __("Tenant"),
            "fieldtype": "Link",
            "options":"Tenant"
        }
	]
};
