def validate_password():
    password = input("Enter a password: ")
    
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    elif not any(char.isdigit() for char in password):
        print("Password must contain at least one number.")
    elif not any(char.isalpha() for char in password):
        print("Password must contain at least one letter.")
    else:
        print("Password is valid.")

validate_password()
