class SearchContact:
    @staticmethod
    def search_contact(contacts):
        query = input("\nEnter any detail (Name, Phone, Email, Address, etc.) to search: ").strip().lower()
        results = [
            contact
            for contact in contacts
            if query in contact["Name"].lower()
            or query in contact["Phone"]
            or query in contact["Email"].lower()
            or query in contact["Address"].lower()
            or query in contact["Birth Date"]
            or query in contact["Company Name"].lower()
            or query in contact["Position"].lower()
        ]

        if results:
            print("\n--- Search Results ---")
            for contact in results:
                print(
                    f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, "
                    f"Address: {contact['Address']}, Birth Date: {contact['Birth Date']}, "
                    f"Company: {contact['Company Name']}, Position: {contact['Position']}"
                )
        else:
            print("No contacts found.")
