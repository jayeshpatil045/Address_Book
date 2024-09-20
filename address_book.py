'''

@Author: Jayesh Patil
@Date: 2024-09-19
@Last Modified by: Jayesh Patil
@Title: Address Book Problem


'''
import logger
from regex_validation import *

logger = logger.logger_init('Address Book')

class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        """
        Description:
            Initializes a Contact object with the provided details.

        Parameters:
            first_name (str): First name of the contact.
            last_name (str): Last name of the contact.
            address (str): Address of the contact.
            city (str): City where the contact resides.
            state (str): State where the contact resides.
            zip_code (str): ZIP code of the contact's location.
            phone_number (str): Contact's phone number.
            email (str): Contact's email address.

        Returns:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        """
        Description:
            Provides a string representation of the Contact object.

        Parameters:
            None

        Returns:
            str: A formatted string that contains the contact's details.
        """
        return (f"Name: {self.first_name} {self.last_name}\n"
                f"Address: {self.address}, {self.city}, {self.state} {self.zip_code}\n"
                f"Phone: {self.phone_number}\nEmail: {self.email}\n")


class AddressBook:
    def __init__(self):
        """
        Description:
            Initializes an empty AddressBook with no contacts.

        Parameters:
            None

        Returns:
            None
        """
        self.contacts = []

    def add_contact(self, contact):
        """
        Description:
            Adds a new Contact object to the address book.

        Parameters:
            contact (Contact): The Contact object to be added to the address book.

        Returns:
            None
        """
        self.contacts.append(contact)
        logger.info(f"Added new contact: {contact.first_name} {contact.last_name}")

    def view_contacts(self):
        """
        Description:
            Displays all contacts in the address book.

        Parameters:
            None

        Returns:
            None
        """
        if not self.contacts:
            logger.info("No contacts to display")
        else:
            for contact in self.contacts:
                logger.info(f"Contact: {contact}")


def main():
    """
    Description:
        Main function that provides a menu-driven interface for the user to add contacts,
        view all contacts, or exit the program. It also validates user inputs for each field.

    Parameters:
        None

    Returns:
        None
    """
    address_book = AddressBook()

    while True:
        logger.info("\n1. Add Contact\n2. View Contacts\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            first_name = input("Enter First Name: ")
            if not validate_first_name(first_name):
                logger.warning(f"Invalid First Name entered: {first_name}")
                continue

            last_name = input("Enter Last Name: ")
            if not validate_last_name(last_name):
                logger.warning(f"Invalid Last Name entered: {last_name}")
                continue

            address = input("Enter Address: ")
            if not validate_address(address):
                logger.warning(f"Invalid Address entered: {address}")
                continue

            city = input("Enter City: ")
            if not validate_city(city):
                logger.warning(f"Invalid City entered: {city}")
                continue

            state = input("Enter State: ")
            if not validate_state(state):
                logger.warning(f"Invalid State entered: {state}")
                continue

            zip_code = input("Enter ZIP Code: ")
            if not validate_zip_code(zip_code):
                logger.warning(f"Invalid ZIP Code entered: {zip_code}")
                continue

            phone_number = input("Enter Phone Number: ")
            if not validate_phone_number(phone_number):
                logger.warning(f"Invalid Phone Number entered: {phone_number}")
                continue

            email = input("Enter Email: ")
            if not validate_email(email):
                logger.warning(f"Invalid Email entered: {email}")
                continue

            contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
            address_book.add_contact(contact)

        elif choice == "2":
            logger.info("User chose to view contacts")
            address_book.view_contacts()

        elif choice == "3":
            logger.info("Program exited by the user")
            break

        else:
            logger.error(f"Invalid choice entered: {choice}")


if __name__ == "__main__":
    main()
