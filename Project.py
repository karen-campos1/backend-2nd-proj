import re

contacts = {}


def is_valid_email(email):
    # Regular expression for validating email addresses
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email)

def is_valid_phone_number(phone_number):
    phone_pattern = r'^\d{3}-\d{3}-\d{4}$'
    return re.match(phone_pattern, phone_number)

def add_contact():
    global contacts
    while True:
        email = input("Enter the e-mail address: ").lower()
        if is_valid_email(email):
            break
        else:
            print("Invalid email format. Please enter a valid email address.")        
    while True:
        phone_num = input("Enter the phone number (following this format 555-555-5555): ")
        if is_valid_phone_number(phone_num):
            break
        else:
            print("Invalid phone number format. Please enter a valid phone number.")
    name = input("Enter the contact's first and last name: ").lower()
    if email not in contacts:
        contacts[email] = {"Phone Number": phone_num, "Name": name, "E-mail": email}
    else:
        print("A contact with this email already exists.")


def edit_contact():
    global contacts
    email = input("Enter the e-mail address for the contact you would like to change: ").lower()
    if email in contacts:
        while True:
            choice = input(str("""\nChoose the information to edit:
    1- Email
    2- Name
    3- Phone Number
    Choice: """)).lower()
            if choice == "1":
                new_email = input("Enter the new email address: ").lower()
                if is_valid_email(new_email):
                    contact_info = contacts.pop(email)
                    contact_info['E-mail'] = new_email
                    contacts[new_email] = contact_info
                    print("Contact edited successfully!")
                    break
                else:
                    print("Invalid email format. Please enter a valid email address.")
            elif choice == "2":
                new_name = input("Enter the new name: ").lower()
                contact_info = contacts[email]
                contact_info['Name'] = new_name
                print("Contact edited successfully!")
                break
            elif choice == "3":
                new_phone_num = input("Enter the new phone number: ")
                if is_valid_phone_number(new_phone_num):
                    contact_info = contacts[email]
                    contact_info['Phone Number'] = new_phone_num
                    print("Contact edited successfully!")
                    break
                else:
                    print("Invalid phone number format. Please enter a valid phone number.")
            else:
                print("Invalid choice. Please enter a number from 1 to 3.")
    else:
        print("Contact not found.")          
            
        
def delete_contact():
    global contacts
    email = input("Enter the e-mail address of the contact you want to delete: ").lower()
    if email in contacts:
        verify = input(f"Are you sure you want to delete this contact {email}? y/n: ").lower()
        if verify == "y":
            del contacts[email]
        elif verify == "n":
            print("You're being directed back to the main menu. Nothing was deleted.")
            return
    else:
        print("Contact not found.")

def search_contact():
    global contacts
    email = input("Enter the e-mail address of the contact you want to search for: ").lower()
    if email in contacts:
        print("Contact found:")
        print("Name:", contacts[email]["Name"])
        print("Phone Number:", contacts[email]["Phone Number"])
        print("E-mail:", contacts[email]["E-mail"])
    else:
        print("Contact not found.")

def display_contacts():
    global contacts
    if contacts:
        print("List of all contacts:")
        for email, contact_info in contacts.items():
            print(f"Email: {email}")
            print(f"Name: {contact_info['Name']}")
            print(f"Phone Number: {contact_info['Phone Number']}")
            print(f"Additional Information: {contact_info.get('Additional Information', 'N/A')}")
            print("------------------------")
    else:
        print("No contacts found.")

def export_contacts():
    pass

def import_contact():
    pass


def run_contact_manager():
    print ("\nWelcome to the Contact Manager App!")
    while True:
        print("\n")
        choice = input("""Please select one of the following options:
                1- Add a new contact
                2- Edit an existing contact
                3- Delete a contact
                4- Search for a contact
                5- Display all contacts
                6- Export contacts to a text file
                7- Import contacts from a text file *BONUS
                8- Quit \nChoice: """)
        if choice == "1":
            add_contact()
            print("You successfully added a contact!")
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact()
            print("Contact deleted successfully!")
        elif choice == "4":
            search_contact()
        elif choice == "5":
            display_contacts()
        elif choice == "6":
            export_contacts()
            print("You successfully exported your contacts.")
        elif choice == "7":
            import_contact()
            print("You successfully imported your contacts into the app.")
        elif choice == "8":
            print("Exiting the program...")
            break
        else:
            print("INVALID CHOICE. Please enter a number from 1 to 8.")          
run_contact_manager()