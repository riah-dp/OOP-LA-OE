print("Name: Moriah De Pedro")
print("=== OE #2 ===\n")

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}"

    def modify_brand(self, new_brand):
        self.brand = new_brand

    def modify_model(self, new_model):
        self.model = new_model

    def modify_price(self, new_price):
        self.price = new_price

def display_phones(phones):
    if phones:
        print("Current Phones:")
        for i, phone in enumerate(phones):
            print(f"{i+1}. {phone}")
    else:
        print("No phones in the list.")

def create_phone(phones):
    brand = input("Enter phone brand: ")
    model = input("Enter phone model: ")
    price = float(input("Enter phone price: "))
    phones.append(Phone(brand, model, price))
    print("Phone added successfully!")

def modify_phone(phones):
    display_phones(phones)
    if phones:
        choice = int(input("Enter the number of the phone to modify: ")) - 1
        if 0 <= choice < len(phones):
            phone = phones[choice]
            print("1. Modify brand")
            print("2. Modify model")
            print("3. Modify price")
            option = int(input("Enter your choice: "))
            if option == 1:
                new_brand = input("Enter new brand: ")
                phone.modify_brand(new_brand)
            elif option == 2:
                new_model = input("Enter new model: ")
                phone.modify_model(new_model)
            elif option == 3:
                new_price = float(input("Enter new price: "))
                phone.modify_price(new_price)
            else:
                print("Invalid choice.")
            print("Phone modified successfully!")
        else:
            print("Invalid phone number.")
    else:
        print("No phones to modify.")

def delete_phone(phones):
    display_phones(phones)
    if phones:
        choice = int(input("Enter the number of the phone to delete: ")) - 1
        if 0 <= choice < len(phones):
            del phones[choice]
            print("Phone deleted successfully!")
        else:
            print("Invalid phone number.")
    else:
        print("No phones to delete.")

def main():
    phones = []
    while True:
        print("\nPhone Management System")
        print("1. Create a phone")
        print("2. Modify a phone")
        print("3. Delete a phone")
        print("4. Display phones")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_phone(phones)
        elif choice == 2:
            modify_phone(phones)
        elif choice == 3:
            delete_phone(phones)
        elif choice == 4:
            display_phones(phones)
        elif choice == 5:
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()