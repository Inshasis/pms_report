// Copyright (c) 2024, Huda Infotech and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Expense Analysis Report"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"reqd": 1,
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"reqd": 1,
			"default": frappe.datetime.get_today(),
		},
		{
			"fieldname": "account",
			"label": __("Expense Account"),
			"fieldtype": "Link",
			"options": "Account",
		},
	],

	// "formatter": function (value, row, column, data, default_formatter) {
	// 	// Add custom formatting if needed
	// 	if (column.fieldname === "total_amount" || column.fieldname === "average_amount") {
	// 		return format_currency(value, "");
	// 	}

	// 	return default_formatter(value, row, column, data);
	// },
	
};
