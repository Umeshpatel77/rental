#empty paste




# Copyright (c) 2024, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RideOrder(Document):
	def validate(self):
		# Jab aap Save button dabayenge tab ye function chalega
		pass

	def on_submit(self):
		# Agar aapne Doctype mein "Is Submittable" check kiya hai
		pass
