def calculate_simple_interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period in years: "))
    
    interest = (principal * rate * time) / 100
    print(f"The simple interest is: {interest}")

calculate_simple_interest()
