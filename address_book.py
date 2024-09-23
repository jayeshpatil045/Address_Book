'''
@Author: Jayesh Patil
@Date: 2024-09-19
@Last Modified by: Jayesh Patil
@Title: Address Book Problem 
'''
import os
import logger
import json
from regex_validation import *

logger = logger.logger_init('Address Book Probelm')

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
        
        return(f"{self.first_name},{self.last_name},{self.address},{self.city},{self.state},"
               f"{self.zip_code},{self.phone_number},{self.email}\n")


class AddressBook:
    def __init__(self, name):
        """
        Description:
            Initializes an AddressBook object with a unique name and an empty contact list.

        Parameters:
            name (str): The name of the Address Book.

        Returns:
            None
        """
        self.name = name
        self.contacts = []
        
    def is_duplicate(self, first_name, last_name):
        """
        Description:
            Checks if a contact with the same first name and last name already exists in the Address Book.

        Parameters:
            first_name (str): The first name of the contact to check.
            last_name (str): The last name of the contact to check.

        Returns:
            bool: True if a duplicate exists, False otherwise.
        """
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return True
        return False

    def add_contact(self, contact):
        """
        Description:
            Adds a new Contact object to the address book after checking for duplicates.
            If a contact with the same name already exists, it prevents the addition.

        Parameters:
            contact (Contact): The Contact object to be added to the address book.

        Returns:
            None
        """
        if self.is_duplicate(contact.first_name, contact.last_name):
            logger.warning(f"Duplicate contact found: {contact.first_name} {contact.last_name}")
            print(f"Contact '{contact.first_name} {contact.last_name}' already exists in the Address Book.")
        else:
            self.contacts.append(contact)
            logger.info(f"Added new contact: {contact.first_name} {contact.last_name}")
            print(f"Contact '{contact.first_name} {contact.last_name}' added successfully.")


    def edit_contact_by_name(self, first_name, last_name):
        """
        Description:
            Edits an existing contact's details based on the provided first and last name.

        Parameters:
            first_name (str): The first name of the contact to be edited.
            last_name (str): The last name of the contact to be edited.

        Returns:
            None
        """
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                logger.info(f"Editing contact: {contact.first_name} {contact.last_name} in Address Book: {self.name}")

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

        logger.error(f"No contact found with the name {first_name} {last_name} in Address Book: {self.name}")
        print(f"No contact found with the name {first_name} {last_name}")

    def delete_contact_by_name(self, first_name, last_name):
        """
        Description:
            Deletes a contact from the Address Book based on the provided first and last name.

        Parameters:
            first_name (str): The first name of the contact to be deleted.
            last_name (str): The last name of the contact to be deleted.

        Returns:
            None
        """
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                self.contacts.remove(contact)
                logger.info(f"Deleted contact: {contact.first_name} {contact.last_name} from Address Book: {self.name}")
                return
        logger.error(f"No contact found with the name {first_name} {last_name} in Address Book: {self.name}")

    def view_contacts(self):
        """
        Description:
            Displays all contacts in the Address Book.

        Parameters:
            None

        Returns:
            None
        """
        if not self.contacts:
            logger.info(f"No contacts to display in Address Book: {self.name}")
            print(f"No contacts available in Address Book: {self.name}.")
        else:
            for contact in self.contacts:
                print(contact)
                logger.info(f"Displayed contact: {contact.first_name} {contact.last_name} from Address Book: {self.name}")

    def sort_contacts(self, by="name"):
        """
        Description:
            Sorts the contacts by a specified attribute: 'name', 'city', 'state', or 'zip'.
        Parameters:
            None

        Returns:
            None    
        """
        if not self.contacts:
            print(f"No contacts available in Address Book: {self.name} to sort.")
            logger.info(f"No contacts available in Address Book: {self.name} to sort.")
        else:
            if by == "name":
                self.contacts.sort(key=lambda contact: (contact.first_name, contact.last_name))
                logger.info(f"Sorted contacts by name in Address Book: {self.name}")
            elif by == "city":
                self.contacts.sort(key=lambda contact: contact.city)
                logger.info(f"Sorted contacts by city in Address Book: {self.name}")
            elif by == "state":
                self.contacts.sort(key=lambda contact: contact.state)
                logger.info(f"Sorted contacts by state in Address Book: {self.name}")
            elif by == "zip":
                self.contacts.sort(key=lambda contact: contact.zip_code)
                logger.info(f"Sorted contacts by ZIP code in Address Book: {self.name}")
            else:
                print("Invalid sort option.")
                return

            print(f"Contacts in Address Book: {self.name} have been sorted by {by}.")

    def load_contacts(self, filename):
        """
        Description:
            Load contacts from a text file.
        Parameters:
            None

        Returns:
            None     
        """
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                for line in file:
                    first_name, last_name, address, city, state, zip_code, phone_number, email = line.strip().split(',')
                    contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
                    self.contacts.append(contact)
            logger.info(f"Loaded {len(self.contacts)} contacts from {filename}.")
        else:
            logger.warning(f"File {filename} does not exist.")

    def save_contacts(self, filename,file_format):
        """
        Description:
            save contacts as text file.
        Parameters:
            None

        Returns:
            None     
        """
        if file_format == "txt":
            if not filename.endswith(".txt"):
                filename += ".txt"
            mode = 'a' if os.path.exists(filename) else 'w'
            with open(filename, mode) as file:
                for contact in self.contacts:
                    file.write(str(contact))
            logger.info(f"Saved {len(self.contacts)} contacts to {filename}.")

        elif file_format == "csv":
            if not filename.endswith(".csv"):
                filename += ".csv"
            mode = 'a' if os.path.exists(filename) else 'w'
            with open(filename, mode) as file:
                if mode == 'w':  
                    file.write("First Name,Last Name,Address,City,State,Zip Code,Phone Number,Email\n")
                for contact in self.contacts:
                    file.write(f"{contact.first_name},{contact.last_name},{contact.address},"
                               f"{contact.city},{contact.state},{contact.zip_code},{contact.phone_number},"
                               f"{contact.email}\n")
            logger.info(f"Saved {len(self.contacts)} contacts to {filename}.")

        elif file_format == "json":
            if not filename.endswith(".json"):
                filename += ".json"
            mode = 'a' if os.path.exists(filename) else 'w'

            with open(filename, mode) as file:
                contacts_dict = [contact.to_dict() for contact in self.contacts]
                json.dump(contacts_dict, file, indent=4)
            logger.info(f"Saved {len(self.contacts)} contacts to {filename} in JSON format.")    
       

class AddressBookSystem:
    def __init__(self):
        """
        Description:
            Initializes the AddressBookSystem with an empty dictionary to store multiple Address Books.

        Parameters:
            None

        Returns:
            None
        """
        self.address_books = {}

    def add_address_book(self, book_name):
        """
        Description:
            Adds a new Address Book to the system with a unique name.

        Parameters:
            book_name (str): The name of the Address Book to be added.

        Returns:
            None
        """
        if book_name in self.address_books:
            logger.error(f"Address Book with the name '{book_name}' already exists.")
            print(f"Address Book '{book_name}' already exists.")
        else:
            self.address_books[book_name] = AddressBook(book_name)
            logger.info(f"Created new Address Book: {book_name}")

    def get_address_book(self, book_name):
        """
        Description:
            Retrieves an Address Book by its name.

        Parameters:
            book_name (str): The name of the Address Book to retrieve.

        Returns:
            AddressBook: The AddressBook object if found, or None if not found.
        """
        return self.address_books.get(book_name, None)

    def search_person_by_city_or_state(self, location, search_type='city'):
        """
        Description:
            Searches for a person by city or state across all address books in the system.

        Parameters:
            location (str): The city or state to search for.
            search_type (str): The type of search ('city' or 'state'). Defaults to 'city'.

        Returns:
            None
        """
        found = False
        logger.info(f"Searching for persons in {search_type.title()}: {location}")
        print(f"Searching for persons in {search_type.title()}: {location}")

        for book_name, address_book in self.address_books.items():
            print(f"\nSearching in Address Book: {book_name}")
            for contact in address_book.contacts:
                if (search_type == 'city' and contact.city == location) or \
                   (search_type == 'state' and contact.state == location):
                    print(contact)
                    logger.info(f"Found contact in {book_name}: {contact.first_name} {contact.last_name}")
                    found = True

        if not found:
            print(f"No contacts found in {search_type.title()} '{location}'.")
            logger.info(f"No contacts found in {search_type.title()} '{location}'.")
    def count_person_by_city_or_state(self, location, search_type='city'):
        """
        Description:
            Counts the number of persons by city or state across all address books in the system.

        Parameters:
            location (str): The city or state to count for.
            search_type (str): The type of search ('city' or 'state'). Defaults to 'city'.

        Returns:
            None
        """
        count = 0
        logger.info(f"Counting persons in {search_type.title()}: {location}")
        print(f"Counting persons in {search_type.title()}: {location}")

        for book_name, address_book in self.address_books.items():
            for contact in address_book.contacts:
                if (search_type == 'city' and contact.city == location) or \
                   (search_type == 'state' and contact.state == location):
                    count += 1

        if count > 0:
            print(f"Total number of contacts in {search_type.title()} '{location}': {count}")
            logger.info(f"Total contacts found in {search_type.title()} '{location}': {count}")
        else:
            print(f"No contacts found in {search_type.title()} '{location}'.")
            logger.info(f"No contacts found in {search_type.title()} '{location}'.")
    



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
        Main function that provides a menu-driven interface for managing multiple Address Books,
        adding contacts, editing, deleting, and viewing contacts within selected Address Books.

    Parameters:
        None

    Returns:
        None
    """
    address_book_system = AddressBookSystem()

    while True:
        print("***************************************************************")
        print("                     Address Book System                       ")
        print("***************************************************************")

        logger.info("\n1. Create Address Book\n2. Select Address Book\n3. Search Person by City\n4. Search Person by State\n5. Count Persons by City\n6. Count Persons by State\n7. Exit")
        choice = input("Enter your choice (1 - 7): ")

        if choice == "1":
            book_name = input("Enter the name for the new Address Book: ")
            address_book_system.add_address_book(book_name)

        elif choice == "2":
            if not address_book_system.address_books:
                logger.info("No Address Books available to select.")
                print("No Address Books available. Please create one first.")
            else:
                print("\nAvailable Address Books:")
                logger.info("Showing available Address Books.")
                
                for book_name in address_book_system.address_books:
                    print(f"- {book_name}")
                
                book_name = input("Enter the name of the Address Book to select: ")
                selected_book = address_book_system.get_address_book(book_name)

                if selected_book:
                    while True:
                        logger.info(f"\nAddress Book: {book_name}\n1. Add Contact\n2. Edit Contact\n3. View Contacts\n4. Delete Contact\n5. Sort Contacts \n6. Manage File \n7. Go Back")
                        sub_choice = input("Enter your choice (1 - 6): ")

                        if sub_choice == "1":
                            first_name = input("Enter First Name: ")
                            if not validate_first_name(first_name):
                                logger.warning(f"Invalid First Name entered: {first_name}  Uppercase letter and is at least 3 characters")
                                continue

                            last_name = input("Enter Last Name: ")
                            if not validate_last_name(last_name):
                                logger.warning(f"Invalid Last Name entered: {last_name}  uppercase letter and is at least 3 characters")
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
                                logger.warning(f"Invalid ZIP Code entered: {zip_code} Ensure it consists of exactly 6 digits.")
                                continue

                            phone_number = input("Enter Phone Number: ")
                            if not validate_phone_number(phone_number):
                                logger.warning(f"Invalid Phone Number entered: {phone_number} It starts with a 2-digit country code, followed by a space, and then a 10-digit number")
                                continue

                            email = input("Enter Email: ")
                            if not validate_email(email):
                                logger.warning(f"Invalid Email entered: {email} It follows a standard email format (e.g., user@domain.com)")
                                continue

                            new_contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
                            selected_book.add_contact(new_contact)

                        elif sub_choice == "2":
                            first_name = input("Enter First Name of the Contact to Edit: ")
                            last_name = input("Enter Last Name of the Contact to Edit: ")
                            selected_book.edit_contact_by_name(first_name, last_name)

                        elif sub_choice == "3":
                            selected_book.view_contacts()

                        elif sub_choice == "4":
                            first_name = input("Enter First Name of the Contact to Delete: ")
                            last_name = input("Enter Last Name of the Contact to Delete: ")
                            selected_book.delete_contact_by_name(first_name, last_name)

                        elif sub_choice == "5":
                            while True:
                                print("\nSort Contacts Menu:\n1. Sort by Name\n2. Sort by City\n3. Sort by State\n4. Sort by ZIP Code\n5. Go Back")
                                sort_choice = input("Enter your choice (1 - 5): ")

                                if sort_choice == "1":
                                    selected_book.sort_contacts(by="name")
                                elif sort_choice == "2":
                                    selected_book.sort_contacts(by="city")
                                elif sort_choice == "3":
                                    selected_book.sort_contacts(by="state")
                                elif sort_choice == "4":
                                    selected_book.sort_contacts(by="zip")
                                elif sort_choice == "5":
                                    break  
                                else:
                                    print("Invalid choice.")
                                    logger.warning(f"Invalid sort choice entered: {sort_choice}")
                        elif sub_choice == "6":  
                            while True:
                                print("\nManage File Menu:\n1. Load Contacts\n2. Save Contacts\n3. Go Back")
                                file_choice = input("Enter your choice (1 - 3): ")

                                if file_choice == "1":
                                    filename = input("Enter the filename to load contacts from: ")
                                    selected_book.load_contacts(filename)

                                elif file_choice == "2":
                                    print("\n File Save Menu:\n1. Save as txt\n2. Save as csv\n3. Save as json\n4. Go Back ")
                                    file_type = input("Enter the file save type(1-4)")
                                    if file_type == "1":
                                        filename = input("Enter the filename to save contacts to: ")
                                        selected_book.save_contacts(filename,"txt")
                                    elif file_type == "2":
                                        filename = input("Enter the filename to save contacts to: ")
                                        selected_book.save_contacts(filename,"csv")
                                    elif file_type == "3":
                                        filename = input("Enter the filename to save contacts to: ")
                                        selected_book.save_contacts(filename,"json")    
                                    else:
                                        break       
                                         
                                elif file_choice == "3":
                                    break
                                else:
                                    print("Invalid choice.")
                                    logger.warning(f"Invalid file choice entered: {file_choice}")            

                        elif sub_choice == "7":
                            break
                        else:
                            logger.warning(f"Invalid choice entered: {sub_choice}")
                else:
                    logger.error(f"No Address Book found with the name: {book_name}")

        elif choice == "3":
            location = input("Enter the City to search: ")
            address_book_system.search_person_by_city_or_state(location, search_type='city')

        elif choice == "4":
            location = input("Enter the State to search: ")
            address_book_system.search_person_by_city_or_state(location, search_type='state')


        elif choice == "5":
            location = input("Enter the City to count: ")
            address_book_system.count_person_by_city_or_state(location, search_type='city')

        elif choice == "6":
            location = input("Enter the State to count: ")
            address_book_system.count_person_by_city_or_state(location, search_type='state')

        elif choice == "7":
            logger.info("Exiting the program.")
            print("Goodbye!")
            break
if __name__ == "__main__":
    main()