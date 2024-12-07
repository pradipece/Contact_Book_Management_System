class UpdateContact:
    @staticmethod
    def update_contact(contacts, file_handler):
        print("\n--- Update Contact ---")
        identifier = input("Enter the Phone Number or Email of the contact to update: ").strip()

        # Find the contact to update
        contact_to_update = None
        for contact in contacts:
            if contact["Phone"] == identifier or contact["Email"].lower() == identifier.lower():
                contact_to_update = contact
                break

        if not contact_to_update:
            print("No contact found with the provided Phone Number or Email.")
            return

        print("\nCurrent Contact Details:")
        print(
            f"Name: {contact_to_update['Name']}, Phone: {contact_to_update['Phone']}, "
            f"Email: {contact_to_update['Email']}, Address: {contact_to_update['Address']}, "
            f"Birth Date: {contact_to_update['Birth Date']}, Company: {contact_to_update['Company Name']}, "
            f"Position: {contact_to_update['Position']}"
        )

        print("\n--- Enter New Details (Leave blank to keep current value) ---")
        name = input(f"Name [{contact_to_update['Name']}]: ").strip()
        phone = input(f"Phone Number [{contact_to_update['Phone']}]: ").strip()
        email = input(f"Email [{contact_to_update['Email']}]: ").strip()
        address = input(f"Address [{contact_to_update['Address']}]: ").strip()
        birth_date = input(f"Birth Date (YYYY-MM-DD) [{contact_to_update['Birth Date']}]: ").strip()
        company_name = input(f"Company Name [{contact_to_update['Company Name']}]: ").strip()
        position = input(f"Position [{contact_to_update['Position']}]: ").strip()

        # Validation
        from prevent_duplicate import PreventDuplicate  # Importing validation class

        if name and not PreventDuplicate.is_valid_name(name):
            print("Invalid name. Please enter a valid string.")
            return
        if phone and not PreventDuplicate.is_valid_phone(phone):
            print("Invalid phone number. Please enter numeric values only.")
            return
        if phone and PreventDuplicate.is_phone_duplicate(phone, contacts) and phone != contact_to_update["Phone"]:
            print("Error: This phone number is already assigned to another contact.")
            return
        if email and not PreventDuplicate.is_valid_email(email):
            print("Invalid email. Please enter a valid email address.")
            return
        if email and PreventDuplicate.is_email_duplicate(email, contacts) and email.lower() != contact_to_update["Email"].lower():
            print("Error: This email is already assigned to another contact.")
            return

        # Update contact details
        contact_to_update["Name"] = name if name else contact_to_update["Name"]
        contact_to_update["Phone"] = phone if phone else contact_to_update["Phone"]
        contact_to_update["Email"] = email if email else contact_to_update["Email"]
        contact_to_update["Address"] = address if address else contact_to_update["Address"]
        contact_to_update["Birth Date"] = birth_date if birth_date else contact_to_update["Birth Date"]
        contact_to_update["Company Name"] = company_name if company_name else contact_to_update["Company Name"]
        contact_to_update["Position"] = position if position else contact_to_update["Position"]

        # Save changes
        file_handler.save_contacts(contacts)
        print("Contact updated successfully!")

