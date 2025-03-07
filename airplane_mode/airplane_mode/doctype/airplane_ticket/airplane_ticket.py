import frappe
import random
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document



class AirplaneTicket(Document):

    def validate(self):
        add_on_types = set()
        total_add_on_amount = 0
        for add_on in self.add_ons:
            # Check for duplicate add-on items
            if add_on.item in add_on_types:
                frappe.throw(f"Duplicate Add-on Type '{add_on.item}' is not allowed!")

            add_on_types.add(add_on.item)  # Mark as seen
            total_add_on_amount += add_on.amount  # Add add-on price to total

        # Calculate Total Amount: Flight Price + Add-ons
        self.total_amount = self.flight_price + total_add_on_amount
        if not self.route:
            self.route = f"/flights/{self.name}"

    def before_submit(self):
        random_number = random.randint(1, 99)
        random_letter = random.choice(["A", "B", "C", "D", "E"])
        self.seat = f"{random_number}{random_letter}"
