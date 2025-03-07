import frappe
import random


def execute():
    # Fetch all Airplane Ticket documents where the seat field is empty or null
    tickets = frappe.get_all(
        "Airplane Ticket", filters={"seat": ("in", ["", None])}, fields=["name"]
    )

    for ticket in tickets:
        doc = frappe.get_doc("Airplane Ticket", ticket.name)
        if not doc.seat:
            random_number = random.randint(1, 99)  # Random integer between 1 and 99
            random_letter = random.choice(
                ["A", "B", "C", "D", "E"]
            )  # Random letter from A to E
            doc.seat = f"{random_number}{random_letter}"
            doc.save(ignore_permissions=True)
