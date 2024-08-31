import random

def generate_random_number():
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))
    
    number = random.randint(lower, upper)
    print(f"Random number between {lower} and {upper} is: {number}")

generate_random_number()
