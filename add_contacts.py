from prevent_duplicate import PreventDuplicate

class AddContact:
    @staticmethod
    def add_contact(contacts, file_handler):
        print("\n--- Add a New Contact ---")
        name = input("Name: ")
        phone = input("Phone Number: ")  # Store phone number as a string to display 0 at beginning
        try:
            email = str(input("Email: "))
            address = str(input("Address: "))
            company_name = str(input("Company Name: "))
            position = str(input("Position: "))
            birth_date = str(input("Birth Date (YYYY-MM-DD): "))
        except ValueError:
            print("Invalid input. Please enter valid values for all fields.")
            return

        # Validation
        if not PreventDuplicate.is_valid_name(name):
            print("Invalid name. Please enter a valid string.")
            return
        if not PreventDuplicate.is_valid_phone(phone):
            print("Invalid phone number. Please enter numeric values only.")
            return
        if PreventDuplicate.is_phone_duplicate(phone, contacts):
            print("Error: This phone number is already assigned to another contact.")
            return
        if not PreventDuplicate.is_valid_email(email):
            print("Invalid email. Please enter a valid email address.")
            return
        if PreventDuplicate.is_email_duplicate(email, contacts):
            print("Error: This email is already assigned to another contact.")
            return

        # Add the contact
        contact = {
            "Name": name,
            "Phone": phone,  # Store phone number as a string
            "Email": email,
            "Address": address,
            "Birth Date": birth_date,
            "Company Name": company_name,
            "Position": position,
        }
        contacts.append(contact)
        file_handler.save_contacts(contacts)
        print(f"Contact {name} added successfully!")
