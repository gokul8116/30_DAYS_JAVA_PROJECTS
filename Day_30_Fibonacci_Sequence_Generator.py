def fibonacci_sequence():
    terms = int(input("Enter the number of terms: "))
    n1, n2 = 0, 1
    count = 0
    
    print("Fibonacci Sequence:")
    while count < terms:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

fibonacci_sequence()
