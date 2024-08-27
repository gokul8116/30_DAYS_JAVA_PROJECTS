def is_palindrome(s):
    return s == s[::-1]

def main():
    print("Palindrome Checker")
    string = input("Enter a string: ").replace(" ", "").lower()
    if is_palindrome(string):
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")

if __name__ == "__main__":
    main()
