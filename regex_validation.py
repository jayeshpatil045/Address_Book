import re

def validate_first_name(first_name):
    return re.match(r"^[A-Z][a-zA-Z]{2,}$", first_name)

def validate_last_name(last_name):
    return re.match(r"^[A-Z][a-zA-Z]{2,}$", last_name)

def validate_address(address):
    return re.match(r'^[\w\s,.-]{5,100}$', address)

def validate_city(city):
    return re.match(r'^[A-Za-z\s]{1,50}$', city)

def validate_state(state):
    return re.match(r'^[A-Za-z\s]{1,50}$', state)

def validate_zip_code(zip_code):
    return re.match(r'^\d{6}$', zip_code)  

def validate_phone_number(phone_number):
    return re.match(r"^\d{2}\s\d{10}$", phone_number)  

def validate_email(email):
    return re.match(r'^[a-zA-Z0-9]+([._%+-][a-zA-Z0-9]+)*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$', email)
