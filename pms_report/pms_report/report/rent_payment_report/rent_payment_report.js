// Copyright (c) 2024, Huda Infotech and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Rent Payment Report"] = {
	"filters": [
		{
			"fieldname":"tenant",
			"label":("Tenant"), // Displayed label for the filter
			"fieldtype":"Link", // Type of the field (Link field, in this case)
			"options":"Customer", // Options for the Link field (referencing the "Item" doctype)
		},
		{
			"fieldname":"property",
			"label":("Property"), // Displayed label for the filter
			"fieldtype":"Link", // Type of the field (Link field, in this case)
			"options":"Item", // Options for the Link field (referencing the "Item" doctype)
		},
	]
};
