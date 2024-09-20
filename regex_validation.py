import re

def validate_first_name(first_name):
    """
    Description:
        Validates the first name to ensure it starts with an uppercase letter and is at least 3 characters long.
    
    Parameters:
        first_name (str): The first name to validate.
    
    Returns:
        bool: True if the first name is valid, False otherwise.
    """
    return re.match(r"^[A-Z][a-zA-Z]{2,}$", first_name)

def validate_last_name(last_name):
    """
    Description:
        Validates the last name to ensure it starts with an uppercase letter and is at least 3 characters long.
    
    Parameters:
        last_name (str): The last name to validate.
    
    Returns:
        bool: True if the last name is valid, False otherwise.
    """
    return re.match(r"^[A-Z][a-zA-Z]{2,}$", last_name)

def validate_address(address):
    """
    Description:
        Validates the address to ensure it is between 5 and 100 characters, allowing letters, numbers, spaces, commas, periods, and hyphens.
    
    Parameters:
        address (str): The address to validate.
    
    Returns:
        bool: True if the address is valid, False otherwise.
    """
    return re.match(r'^[\w\s,.-]{5,100}$', address)

def validate_city(city):
    """
    Description:
        Validates the city name to ensure it only contains letters and spaces, with a length of 1 to 50 characters.
    
    Parameters:
        city (str): The city name to validate.
    
    Returns:
        bool: True if the city name is valid, False otherwise.
    """
    return re.match(r'^[A-Za-z\s]{1,50}$', city)

def validate_state(state):
    """
    Description:
        Validates the state name to ensure it only contains letters and spaces, with a length of 1 to 50 characters.
    
    Parameters:
        state (str): The state name to validate.
    
    Returns:
        bool: True if the state name is valid, False otherwise.
    """
    return re.match(r'^[A-Za-z\s]{1,50}$', state)

def validate_zip_code(zip_code):
    """
    Description:
        Validates the ZIP code to ensure it consists of exactly 6 digits.
    
    Parameters:
        zip_code (str): The ZIP code to validate.
    
    Returns:
        bool: True if the ZIP code is valid, False otherwise.
    """
    return re.match(r'^\d{6}$', zip_code)

def validate_phone_number(phone_number):
    """
    Description:
        Validates the phone number to ensure it starts with a 2-digit country code, followed by a space, and then a 10-digit number.
    
    Parameters:
        phone_number (str): The phone number to validate.
    
    Returns:
        bool: True if the phone number is valid, False otherwise.
    """
    return re.match(r"^\d{2}\s\d{10}$", phone_number)

def validate_email(email):
    """
    Description:
        Validates the email address to ensure it follows a standard email format (e.g., user@domain.com).
    
    Parameters:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    return re.match(r'^[a-zA-Z0-9]+([._%+-][a-zA-Z0-9]+)*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$', email)
