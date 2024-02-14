// Copyright (c) 2024, Huda Infotech and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Maintenance Request Report"] = {
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
            "fieldname": "maintenance_type",
            "label": __("Maintenance Type"),
            "fieldtype": "Link",
            "options": "Issue Type"
        }
    ],
    // "formatter": function(value, row, column, data, default_formatter) {
    //     if (column.df.fieldname == "maintenance_date") {
    //         return frappe.datetime.str_to_user(value);
    //     }
    //     return default_formatter(value, row, column, data);
    // },
}