def is_armstrong():
    num = int(input("Enter a number: "))
    order = len(str(num))
    sum_digits = sum(int(digit) ** order for digit in str(num))
    
    if num == sum_digits:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")

is_armstrong()
