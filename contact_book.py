# Contact Book Management System

contacts = []

# Add Contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    contacts.append(contact)
    print("Contact added successfully!")

# View Contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n----- Contact List -----")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['Name']} - {contact['Phone']}")

# Search Contact
def search_contact():
    key = input("Enter Name or Phone Number: ").lower()

    found = False
    for contact in contacts:
        if key == contact["Name"].lower() or key == contact["Phone"]:
            print("\nContact Found")
            print("Name:", contact["Name"])
            print("Phone:", contact["Phone"])
            print("Email:", contact["Email"])
            print("Address:", contact["Address"])
            found = True

    if not found:
        print("Contact not found.")

# Update Contact
def update_contact():
    phone = input("Enter Phone Number of contact to update: ")

    for contact in contacts:
        if contact["Phone"] == phone:
            contact["Name"] = input("Enter New Name: ")
            contact["Phone"] = input("Enter New Phone Number: ")
            contact["Email"] = input("Enter New Email: ")
            contact["Address"] = input("Enter New Address: ")
            print("Contact updated successfully!")
            return

    print("Contact not found.")

# Delete Contact
def delete_contact():
    phone = input("Enter Phone Number to delete: ")

    for contact in contacts:
        if contact["Phone"] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")

# Main Menu
while True:
    print("\n===== CONTACT BOOK MENU =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Thank you for using Contact Book.")
        break
    else:
        print("Invalid choice! Please try again.")