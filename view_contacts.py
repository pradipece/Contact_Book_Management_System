class ViewContact:
    @staticmethod
    def view_contacts(contacts):
        if not contacts:
            print("\nNo contacts available.")
            return

        print("\n--- Contact List ---")
        for i, contact in enumerate(contacts, start=1):
            print(
                f"{i}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, "
                f"Address: {contact['Address']}, Birth Date: {contact['Birth Date']}, "
                f"Company: {contact['Company Name']}, Position: {contact['Position']}"
            )
