def show_contacts(contacts):
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    print()

def contact_book():
    contacts = {}
    
    while True:
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. View All Contacts")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contacts[name] = {"phone": phone, "email": email}
        elif choice == '2':
            name = input("Enter the name of the contact to delete: ")
            contacts.pop(name, None)
        elif choice == '3':
            name = input("Enter the name of the contact to search: ")
            if name in contacts:
                print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
            else:
                print("Contact not found!")
        elif choice == '4':
            show_contacts(contacts)
        elif choice == '5':
            break
        else:
            print("Invalid option!")

contact_book()
