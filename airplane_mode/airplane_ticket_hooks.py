import frappe


def prevent_submission(doc, method):
    if doc.status != "Boarded":
        frappe.throw(
            "You can't submit this Airplane Ticket because the status is not 'Boarded'."
        )
