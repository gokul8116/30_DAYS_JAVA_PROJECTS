import re

def password_strength_checker():
    password = input("Enter your password: ")
    
    if len(password) < 8:
        print("Password too short! Must be at least 8 characters.")
    elif not re.search(r'[A-Z]', password):
        print("Password must contain at least one uppercase letter.")
    elif not re.search(r'[a-z]', password):
        print("Password must contain at least one lowercase letter.")
    elif not re.search(r'[0-9]', password):
        print("Password must contain at least one number.")
    elif not re.search(r'[@#$%^&*!]', password):
        print("Password must contain at least one special character (@#$%^&*!).")
    else:
        print("Password is strong!")

password_strength_checker()
