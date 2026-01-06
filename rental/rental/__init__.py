import frappe

def execute():
    vehicles =frappe.db.get_all("Vehicle1")
    for v in vehicles:
        vehicle = frappe.get
