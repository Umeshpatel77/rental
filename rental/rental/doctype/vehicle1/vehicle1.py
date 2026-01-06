from frappe.website.website_generator import WebsiteGenerator

class Vehicle1(WebsiteGenerator):
	def before_save(self):
		# self.set_title()
		pass

	def set_title(self):
		self.title = f"{self.make} {self.model}, {self.year}"
