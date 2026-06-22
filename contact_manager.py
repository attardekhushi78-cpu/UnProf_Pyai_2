import json

# Name of our database file
FILE_NAME = "contacts.json"


#  FILE HANDLING CHANNELS (Load & Save)


def load_contacts():
    """Loads contacts from the JSON file safely."""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist yet, return an empty list
        return []
    except json.JSONDecodeError:
        print("⚠️ Warning: File corrupted. Initializing a fresh database.")
        return []

def save_contacts(contacts_list):
    """Saves the entire contacts list to the JSON file."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        # json.dump converts our list of dictionaries into plain text inside the file
        json.dump(contacts_list, file, indent=4)


#  CORE FEATURE FUNCTIONS


def add_new_contact(contacts_list):
    """Prompts user for inputs and appends a new contact dictionary."""
    print("\n--- Create New Contact ---")
    name = input("Enter Full Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email Address: ").strip()
    category = input("Enter Category (e.g., Friends, Work, Family): ").strip()

    # Simple Validation
    if not name or not phone:
        print("❌ Error: Name and Phone Number are mandatory fields!")
        return

    # Check for duplicates
    for contact in contacts_list:
        if contact["name"].lower() == name.lower():
            print(f"❌ Error: A contact named '{name}' already exists.")
            return

    if not category:
        category = "General"

    # Representing our data structure as a plain dictionary
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "category": category
    }

    # Save to dynamic list and sync to local disk storage instantly
    contacts_list.append(new_contact)
    save_contacts(contacts_list)
    print(f"✅ Success: '{name}' added to your contacts!")

def view_all_contacts(contacts_list):
    """Displays all contacts neatly formatted."""
    print("\n--- All Registered Contacts ---")
    if not contacts_list:
        print("Your database is empty.")
        return

    print(f"{'Name':<20} | {'Phone':<15} | {'Email':<25} | {'Category':<12}")
    print("-" * 78)
    for c in contacts_list:
        print(f"{c['name']:<20} | {c['phone']:<15} | {c['email']:<25} | {c['category']:<12}")

def search_contact(contacts_list):
    """Searches for records using a search term."""
    print("\n--- Search Directory ---")
    query = input("Enter name, email, or category keyword to look up: ").strip().lower()

    if not query:
        print("❌ Search cancelled. Empty keyword string.")
        return

    found_any = False
    print(f"\nSearching for parameters matching: '{query}'...")
    print(f"{'Name':<20} | {'Phone':<15} | {'Email':<25} | {'Category':<12}")
    print("-" * 78)

    for c in contacts_list:
        # Look inside each property index row matching text inputs
        if (query in c["name"].lower() or 
            query in c["email"].lower() or 
            query in c["category"].lower()):
            print(f"{c['name']:<20} | {c['phone']:<15} | {c['email']:<25} | {c['category']:<12}")
            found_any = True

    if not found_any:
        print("No matching contact entries found.")


#  MENU DASHBOARD RUNNER LOOP


def main():
    # Load data rows off storage array files on startup
    my_contacts = load_contacts()
    
    print("⚡ Persistent JSON Contact Management System Tool")
    print(f"📁 Linked to active text workspace file index: '{FILE_NAME}'")

    while True:
        print("\n=== Navigation Menu ===")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contacts")
        print("4. Exit System")
        
        choice = input("\nEnter choice number (1-4): ").strip()

        if choice == "1":
            add_new_contact(my_contacts)
        elif choice == "2":
            view_all_contacts(my_contacts)
        elif choice == "3":
            search_contact(my_contacts)
        elif choice == "4":
            print("🚀 Secure database log out sync sequence closed safely. Happy coding!")
            break
        else:
            print("❌ Invalid entry option value tag! Please choose numbers 1 through 4.")

if __name__ == "__main__":
    main()