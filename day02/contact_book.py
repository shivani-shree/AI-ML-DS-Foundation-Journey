# CONTACT BOOK

contacts = {}

while True:

    choice = int(input('''1. Add a contact
    2. Search for a contact
    3. Delete a contact
    4. Exit
    Enter your choice:'''))

    if choice == 1:
        name = input("Enter the name of the person: ").title()
        phone = input("Enter their contact number: ")
        email = input("Enter their email ID: ")
        contacts[name] = {'phone' : phone, 'email' : email}
        print(f"{name} added Successfully!")

    elif choice == 2:
        name = input("Enter the name of the person: ").title()
        if name in contacts:
            print(f"Name: {name} -> Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
        else:
            print(f"{name} is not in saved contacts!")

    elif choice == 3:
        name = input("Enter the name of the person: ").title()
        if name in contacts:
            del contacts[name]
            print(f"{name} deleted!")
        else:
            print(f"{name} is not in saved contacts!")

    elif choice ==  4:
        break

    else:
        print("Enter a valid choice!")
        continue

    