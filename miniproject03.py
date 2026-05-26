#-------------------------------------------------------------------------------------------------------------------

# Miniproject-3:Student Record Manager

#-------------------------------------------------------------------------------------------------------------------


records = {}

while True:
    print("\n--- Student Record Manager ---")
    print("1. Add Record")
    print("2. View Records")
    print("3. Search Record")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        records[phone] = {"Name": name, "Email": email}
        print("Record added successfully!")

    elif choice == "2":
        if not records:
            print("No records found.")
        else:
            for phone, details in records.items():
                print(f"Phone: {phone}, Name: {details['Name']}, Email: {details['Email']}")

    elif choice == "3":
        phone = input("Enter phone to search: ")
        if phone in records:
            print("Record found:", records[phone])
        else:
            print("Record not found.")

    elif choice == "4":
        phone = input("Enter phone to update: ")
        if phone in records:
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            records[phone] = {"Name": name, "Email": email}
            print("Record updated.")
        else:
            print("Record not found.")

    elif choice == "5":
        phone = input("Enter phone to delete: ")
        if phone in records:
            del records[phone]
            print("Record deleted.")
        else:
            print("Record not found.")

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")

print("----------Executed Successfully!!-----------")
