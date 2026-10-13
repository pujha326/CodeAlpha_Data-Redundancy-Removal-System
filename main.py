
import json
import os

FILE = "database.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_data():
    data = load_data()

    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip().lower()

    if not name or not email:
        print("Invalid data! Name and email are required.")
        return

    for record in data:
        if record["email"] == email:
            print("Duplicate data detected! Not saved.")
            return

    data.append({"name": name, "email": email})
    save_data(data)

    print("Unique data saved successfully!")

def view_data():
    data = load_data()

    print("\nStored Records:")
    if not data:
        print("No records found.")
    else:
        for record in data:
            print(record)

while True:
    print("\n--- Data Redundancy Removal System ---")
    print("1. Add Data")
    print("2. View Data")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_data()
    elif choice == "2":
        view_data()
    elif choice == "3":
        print("Program closed.")
        break
    else:
        print("Invalid choice! Try agalin.")

