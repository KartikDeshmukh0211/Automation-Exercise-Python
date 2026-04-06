import random
import string
from datetime import datetime, timedelta


def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_random_email():
    return generate_random_string(6) + "@gmail.com"

def generate_random_password(length=10):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))

def generate_random_name():
    return generate_random_string(8)

def generate_random_phone(lenght=8):
    return ''.join(random.choices(string.digits, k=lenght))

def generate_random_address():
    streets = ["Main St", "Park Ave", "MG Road", "Station Road", "Lake View"]
    cities = ["Mumbai", "Pune", "Delhi", "Bangalore", "Chennai"]
    states = ["Maharashtra", "Karnataka", "Delhi", "Tamil Nadu"]
    
    house_number = random.randint(1, 999)
    street = random.choice(streets)
    city = random.choice(cities)
    state = random.choice(states)
    pincode = ''.join(random.choices(string.digits, k=6))
    
    return f"{house_number}, {street}, {city}, {state} - {pincode}"