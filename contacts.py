import json

FILE = "contacts.json"


def load_contacts():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=2)


def find_name(contacts, name):
    for key in contacts:
        if key.lower() == name.lower():
            return key
    return None


def show_all(contacts):
    if len(contacts) == 0:
        print("No contacts yet!")
        return
    for name in sorted(contacts):
        info = contacts[name]
        print(name, "|", info["phone"], "|", info["email"])


def add_contact(contacts):
    name = input("Name: ").strip()
    if name == "":
        print("Name can't be empty.")
        return
    if find_name(contacts, name) is not None:
        print("That contact already exists.")
        return
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print("Added!")


def search_contacts(contacts):
    term = input("Search for: ").strip().lower()
    found = False
    for name in sorted(contacts):
        if term in name.lower():
            info = contacts[name]
            print(name, "|", info["phone"], "|", info["email"])
            found = True
    if not found:
        print("No match.")


def edit_contact(contacts):
    name = find_name(contacts, input("Which contact to edit? ").strip())
    if name is None:
        print("Contact not found.")
        return
    print("Press Enter to keep the old value.")
    phone = input("New phone: ").strip()
    email = input("New email: ").strip()
    if phone != "":
        contacts[name]["phone"] = phone
    if email != "":
        contacts[name]["email"] = email
    save_contacts(contacts)
    print("Updated!")


def delete_contact(contacts):
    name = find_name(contacts, input("Which contact to delete? ").strip())
    if name is None:
        print("Contact not found.")
        return
    contacts.pop(name)
    save_contacts(contacts)
    print("Deleted!")


contacts = load_contacts()

while True:
    print()
    print("1 = show all, 2 = add, 3 = search, 4 = edit, 5 = delete, 6 = quit")
    choice = input("Pick: ")
    if choice == "1":
        show_all(contacts)
    elif choice == "2":
        add_contact(contacts)
    elif choice == "3":
        search_contacts(contacts)
    elif choice == "4":
        edit_contact(contacts)
    elif choice == "5":
        delete_contact(contacts)
    elif choice == "6":
        print("Bye!")
        break
    else:
        print("Please pick 1 to 6.")