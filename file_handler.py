import csv
import os

class FileHandler:
    FILE_PATH = "data/contacts.csv"

    def load_contacts(self):
        # Create file if it doesn't exist
        if not os.path.exists(self.FILE_PATH):
            os.makedirs(os.path.dirname(self.FILE_PATH), exist_ok=True)
            with open(self.FILE_PATH, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["Name", "Phone", "Email", "Address", "Birth Date", "Company Name", "Position"])
                writer.writeheader()
            return []

        # Load contacts from file
        contacts = []
        with open(self.FILE_PATH, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
        return contacts

    def save_contacts(self, contacts):
        # Save all contacts to file
        with open(self.FILE_PATH, "w", newline="") as file:
            fieldnames = ["Name", "Phone", "Email", "Address", "Birth Date", "Company Name", "Position"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(contacts)

        print(f"{len(contacts)} contacts saved to {self.FILE_PATH}")
