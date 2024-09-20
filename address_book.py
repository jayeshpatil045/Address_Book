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

    def edit_contact_by_name(self, first_name, last_name):
        """
        Description:
            Edits an existing contact's details based on the provided first and last name.

        Parameters:
            first_name (str): First name of the contact to edit.
            last_name (str): Last name of the contact to edit.

        Returns:
            None
        """
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                logger.info(f"Editing contact: {contact.first_name} {contact.last_name}")

                contact.first_name = input_validation("Enter new First Name", contact.first_name, validate_first_name)
                contact.last_name = input_validation("Enter new Last Name", contact.last_name, validate_last_name)
                contact.address = input_validation("Enter new Address", contact.address, validate_address)
                contact.city = input_validation("Enter new City", contact.city, validate_city)
                contact.state = input_validation("Enter new State", contact.state, validate_state)
                contact.zip_code = input_validation("Enter new ZIP Code", contact.zip_code, validate_zip_code)
                contact.phone_number = input_validation("Enter new Phone Number", contact.phone_number, validate_phone_number)
                contact.email = input_validation("Enter new Email", contact.email, validate_email)

                logger.info(f"Updated contact: {contact.first_name} {contact.last_name}")
                return

        logger.error(f"No contact found with the name {first_name} {last_name}")
        print(f"No contact found with the name {first_name} {last_name}")

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
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)
                logger.info(f"Contact displayed: {contact.first_name} {contact.last_name}")


def input_validation(prompt, current_value, validation_function):
    """
    Description:
        Prompts the user for input and validates it using the provided validation function.
        If the user inputs nothing, the current value is retained.

    Parameters:
        prompt (str): The prompt message to display to the user.
        current_value (str): The current value of the field.
        validation_function (function): The function used to validate the user's input.

    Returns:
        str: The validated input from the user or the current value if no input is given.
    """
    while True:
        new_value = input(f"{prompt} [{current_value}]: ")
        if new_value:
            if validation_function(new_value):
                return new_value
            else:
                logger.warning(f"Invalid input for {prompt}: {new_value}")
        else:
            return current_value


def main():
    """
    Description:
        Main function that provides a menu-driven interface for the user to add contacts,
        edit existing contacts, view all contacts, or exit the program.
        It also validates user inputs for each field.

    Parameters:
        None

    Returns:
        None
    """
    address_book = AddressBook()

    while True:
        logger.info("\n1. Add Contact\n2. Edit Contact\n3. View Contacts\n4. Exit")
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
            first_name = input("Enter First Name of the contact to edit: ")
            last_name = input("Enter Last Name of the contact to edit: ")
            address_book.edit_contact_by_name(first_name, last_name)

        elif choice == "3":
            address_book.view_contacts()

        elif choice == "4":
            logger.info("Program exited by the user")
            break

        else:
            logger.error(f"Invalid choice entered: {choice}")


if __name__ == "__main__":
    main()
