import json
import os

class ContactBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email):
        self.contacts[name] = {'phone': phone, 'email': email}
        self.save_contacts()
        print(f"Contact {name} added.")

    def get_contact(self, name):
        return self.contacts.get(name, None)

    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            self.save_contacts()
            print(f"Contact {name} updated.")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Contact {name} deleted.")
        else:
            print(f"Contact {name} not found.")

    def list_contacts(self):
        for name, info in self.contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def main():
    book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Retrieve Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. List Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            book.add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter name: ")
            contact = book.get_contact(name)
            if contact:
                print(f"Name: {name}, Phone: {contact['phone']}, Email: {contact['email']}")
            else:
                print("Contact not found.")
        elif choice == '3':
            name = input("Enter name: ")
            phone = input("Enter new phone (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            book.update_contact(name, phone if phone else None, email if email else None)
        elif choice == '4':
            name = input("Enter name: ")
            book.delete_contact(name)
        elif choice == '5':
            book.list_contacts()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
