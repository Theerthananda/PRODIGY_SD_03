import json

# Function to load contacts from a file
def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)  # Read contacts from the file
    except FileNotFoundError:
        return {}  # Return an empty dictionary if file doesn't exist

# Function to save contacts to a file
def save_contacts(filename, contacts):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)  # Save contacts as JSON

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone number: ").strip()
    email = input("Enter contact email: ").strip()
    
    # Check if contact already exists
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print("Contact added successfully.")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\n---")

# Function to edit an existing contact
def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ").strip()
    if name in contacts:
        phone = input("Enter new phone number (leave blank to keep current): ").strip()
        email = input("Enter new email (leave blank to keep current): ").strip()
        
        # Update phone and email if provided
        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        
        print("Contact updated.")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]  # Remove contact from dictionary
        print("Contact deleted.")
    else:
        print("Contact not found.")

# Main program
def main():
    filename = "contacts.json"
    contacts = load_contacts(filename)  # Load contacts from file

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(filename, contacts)  # Save contacts before exiting
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
