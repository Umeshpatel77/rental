from frappe.model.document import Document
import frappe

class RideBooking(Document):
    def validate(self):
        if not self.rate:
            frappe.throw("Please provide a rate")

        total_distance = 0
        for item in self.items:
            total_distance += item.distance

        self.total_amount = total_distance * self.rate
