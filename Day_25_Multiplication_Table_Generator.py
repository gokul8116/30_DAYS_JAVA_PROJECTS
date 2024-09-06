def multiplication_table():
    num = int(input("Enter a number: "))
    print(f"Multiplication table for {num}:")
    
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

multiplication_table()
