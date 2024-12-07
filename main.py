from add_contacts import AddContact
from view_contacts import ViewContact
from search_contacts import SearchContact
from remove_contacts import RemoveContact
from contact_update import UpdateContact
from file_handler import FileHandler

class ContactBook:
    def __init__(self):
        self.file_handler = FileHandler()
        self.contacts = self.file_handler.load_contacts()
    
    def display_menu(self):
        while True:
            print("\n--- Contact Book Menu ---")
            print("0. Exit")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Remove Contact")
            print("5. Update Contact")
            
            menu = input("Choose an option: ")

            if menu == "0":
                print("Thanks for using Contact Book Management System")
                break
            if menu == "1":
                AddContact.add_contact(self.contacts, self.file_handler)
            elif menu == "2":
                ViewContact.view_contacts(self.contacts)
            elif menu == "3":
                SearchContact.search_contact(self.contacts)
            elif menu == "4":
                RemoveContact.remove_contact(self.contacts, self.file_handler)
            elif menu == "5":
                UpdateContact.update_contact(self.contacts, self.file_handler)
            else:
                print("Invalid menu. Please try again.")

if __name__ == "__main__":
    app = ContactBook()
    app.display_menu()
