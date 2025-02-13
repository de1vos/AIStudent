# Task 3: Functions and Modules
# List of contacts. Each contact is a dictionary with keys 'name', 'phone_number', and 'email'
contacts = []

# Add a contact to the end of the list
def add_contact(name: str, phone_number: str, email: str) -> int:
    contact = { ## Dict with function arguments as components
        "name": name,
        "phone_number": phone_number,
        "email": email
    }
    contacts.append(contact) # Add to list
    contact_id = len(contacts) - 1 # Assign index
    return contact_id # index of the contact in the contacts list

# Update an existing contact
def update_contact(id: int, name: str, phone_number: str, email: str) -> None:
    if 0 <= contact_id < len(contacts):
        contacts[id] = {
            "name": name,
            "phone_number": phone_number,
            "email": email
        }
        print(f"Contact {contact_id} updated successfully")
    else:
        print(f"Incorrect access, nowhere to update {contact_id}")

# Display contacts
def display_contacts():
    for index, x in enumerate(contacts):
        print(f"Contact Information (ID: {index}))")
        for key, value in x.items():
            print(f"{key} : {value}")
        print("")

# Test the functions
contact_id = add_contact("John Doe", "123-456-7890", "john@example.com")
contact2 = add_contact("Alice Smith", "123-456-7777", "alice@example.com")
display_contacts()
update_contact(
    id = contact_id,
    name = "John Smith",
    phone_number = "555-555-5555",
    email = "johnSmith@example.com"
)
display_contacts()