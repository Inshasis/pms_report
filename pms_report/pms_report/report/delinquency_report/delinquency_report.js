// Copyright (c) 2024, Huda Infotech and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Delinquency Report"] = {
	"filters": [
		{
			fieldtype: 'Date',
			label: __('Start Date'),
			fieldname: 'start_date',
			reqd: 1,
			default: frappe.datetime.add_months(frappe.datetime.get_today(), -1)
		},
		{
			fieldtype: 'Date',
			label: __('End Date'),
			fieldname: 'end_date',
			reqd: 1,
			default: frappe.datetime.get_today()
		}

	]
};
