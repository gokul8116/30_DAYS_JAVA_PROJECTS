def character_counter():
    text = input("Enter a string: ")
    count = {}
    
    for char in text:
        count[char] = count.get(char, 0) + 1
    
    for char, cnt in count.items():
        print(f"{char}: {cnt}")

character_counter()
