# ``` Welcome to the Contact Management System! Menu:
# Add a new contact
# Edit an existing contact
# Delete a contact
# Search for a contact
# Display all contacts
# Export contacts to a text file
# Import contacts from a text file *BONUS
# Quit " 


# "someone@gmail.com": {
#      "phone number": "1212312312313",
#      "name": "A name",
#        "email": "someone@gmail.com"

# }



contacts = {}

def add_contact():
    global contacts
    email = input("Enter the e-mail address: ").lower()
    phone_num = input("Enter the phone number (following this format 555-555-5555): ")
    name = input("Enter the contact's first and last name: ").lower()
    if email not in contacts:
        contacts[email] = {"Phone Number": phone_num, "Name": name, "E-mail": email}
        print(contacts) #TO REMOVE
    else:
        print("A contact with this email already exists.")

def edit_contact():
    pass

def delete_contact():
    pass

def search_contact():
    pass

def display_contacts():
    pass

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
            print("You successfully made an edit")
        elif choice == "3":
            delete_contact()
            print("You deleted a contact")
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