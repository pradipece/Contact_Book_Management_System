class PreventDuplicate:
    @staticmethod
    def is_valid_name(name):
        # Check if the name is a non-empty string
        return isinstance(name, str) and name.strip() != ""

    @staticmethod
    def is_valid_phone(phone):
        # Check if the phone number is a string of digits
        return phone.isdigit()

    @staticmethod
    def is_phone_duplicate(phone, contacts):
        # Check if the phone number already exists in the contacts
        for contact in contacts:
            if contact["Phone"] == phone:
                return True
        return False
    
    @staticmethod
    def is_valid_email(email):
        # Check if the email contains '@' and '.' and is not empty
        return isinstance(email, str) and "@" in email and "." in email and email.strip() != ""
    
    @staticmethod
    def is_email_duplicate(email, contacts):
        # Check if the email already exists in the contacts
        for contact in contacts:
            if contact["Email"] == email:
                return True
        return False
