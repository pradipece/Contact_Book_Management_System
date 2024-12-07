class RemoveContact:
    @staticmethod
    def remove_contact(contacts, file_handler):
        phone = input("\nEnter the phone number of the contact to remove: ").strip()
        for contact in contacts:
            if contact["Phone"] == phone:
                contacts.remove(contact)
                file_handler.save_contacts(contacts)
                print(f"Contact with phone {phone} removed successfully!")
                return

        print("No contact found with this phone number.")
