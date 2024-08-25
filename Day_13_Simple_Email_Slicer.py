# User input
email = input("Please enter your email: ").strip()

# Check if email contains '@'
if "@" in email:
    # Defining username and domain parts
    username_part = email[:email.index("@")]
    domain_name = email[email.index("@") + 1:]

    # Generating the output
    output = f"Your username is '{username_part}' and your domain is '{domain_name}'"
else:
    output = "Invalid email format. Please enter a valid email address."

# Print the output
print(output)
