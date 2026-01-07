from frappe.model.document import Document
import frappe

class RideBooking(Document):
    def validate(self):
        # Agar rate empty hai, toh settings se default value lo
        if not self.rate:
            self.rate = frappe.db.get_single_value("Rentals Settings", "standard_rate")

        total_distance = 0
        for item in self.items:
            total_distance += item.distance

        # Total amount = distance * rate
        self.total_amount = total_distance * self.rate
