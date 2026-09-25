# ============================================================
# INVENTORY MANAGEMENT SYSTEM
# ============================================================

# File used to save inventory information
FILE_NAME = "inventory.txt"


# ============================================================
# LOAD INVENTORY
# ============================================================

def load_inventory():

    inventory = []

    try:

        file = open(FILE_NAME, "r")

        line = file.readline()

        while line != "":

            parts = line.split(",")

            if len(parts) == 3:

                name = parts[0]
                quantity = int(parts[1])
                price = float(parts[2])

                item = {
                    "name": name,
                    "quantity": quantity,
                    "price": price
                }

                inventory.append(item)

            line = file.readline()

        file.close()

    except FileNotFoundError:

        file = open(FILE_NAME, "w")
        file.close()

    return inventory


# ============================================================
# SAVE INVENTORY
# ============================================================

def save_inventory(inventory):

    file = open(FILE_NAME, "w")

    index = 0

    while index < len(inventory):

        item = inventory[index]

        file.write(
            item["name"] + ","
            + str(item["quantity"]) + ","
            + str(item["price"]) + "\n"
        )

        index += 1

    file.close()


# ============================================================
# DISPLAY INVENTORY
# ============================================================

def display_inventory(inventory):

    if len(inventory) == 0:

        print("\nInventory is empty.")

    else:

        print("\n" + "=" * 55)
        print("                    INVENTORY")
        print("=" * 55)

        print(
            f"{'Item':<25}"
            f"{'Quantity':<12}"
            f"{'Price':<12}"
        )

        print("-" * 55)

        index = 0

        while index < len(inventory):

            item = inventory[index]

            print(
                f"{item['name']:<25}"
                f"{item['quantity']:<12}"
                f"${item['price']:<11.2f}"
            )

            index += 1

        print("=" * 55)


# ============================================================
# ADD ITEM
# ============================================================

def add_item(inventory):

    print("\n--- Add Item ---")

    name = input("Enter item name: ")

    while name == "":
        print("Item name cannot be empty.")
        name = input("Enter item name: ")

    quantity = input("Enter quantity: ")

    while not quantity.isdigit():

        print("Please enter a valid whole number.")

        quantity = input("Enter quantity: ")

    quantity = int(quantity)

    price = input("Enter price: ")

    while True:

        try:

            price = float(price)

            if price >= 0:
                break

            print("Price cannot be negative.")

        except ValueError:

            print("Please enter a valid price.")

        price = input("Enter price: ")

    item = {
        "name": name,
        "quantity": quantity,
        "price": price
    }

    inventory.append(item)

    save_inventory(inventory)

    print("\nItem added successfully.")


# ============================================================
# SEARCH FOR ITEM
# ============================================================

def search_item(inventory):

    print("\n--- Search Inventory ---")

    search_name = input("Enter item name: ")

    found = False

    index = 0

    while index < len(inventory):

        item = inventory[index]

        if item["name"].lower() == search_name.lower():

            print("\nItem found:")
            print("Name:", item["name"])
            print("Quantity:", item["quantity"])
            print(f"Price: ${item['price']:.2f}")

            found = True

        index += 1

    if not found:

        print("\nItem was not found.")


# ============================================================
# UPDATE ITEM
# ============================================================

def update_item(inventory):

    print("\n--- Update Item ---")

    search_name = input("Enter item name to update: ")

    found = False

    index = 0

    while index < len(inventory):

        item = inventory[index]

        if item["name"].lower() == search_name.lower():

            found = True

            quantity = input("Enter new quantity: ")

            while not quantity.isdigit():

                print("Please enter a valid whole number.")

                quantity = input("Enter new quantity: ")

            item["quantity"] = int(quantity)

            price = input("Enter new price: ")

            while True:

                try:

                    price = float(price)

                    if price >= 0:
                        break

                    print("Price cannot be negative.")

                except ValueError:

                    print("Please enter a valid price.")

                price = input("Enter new price: ")

            item["price"] = price

            save_inventory(inventory)

            print("\nItem updated successfully.")

        index += 1

    if not found:

        print("\nItem was not found.")


# ============================================================
# REMOVE ITEM
# ============================================================

def remove_item(inventory):

    print("\n--- Remove Item ---")

    search_name = input("Enter item name to remove: ")

    found = False

    index = 0

    while index < len(inventory):

        item = inventory[index]

        if item["name"].lower() == search_name.lower():

            inventory.pop(index)

            save_inventory(inventory)

            print("\nItem removed successfully.")

            found = True

            index = len(inventory)

        else:

            index += 1

    if not found:

        print("\nItem was not found.")


# ============================================================
# INVENTORY VALUE
# ============================================================

def calculate_inventory_value(inventory):

    total = 0

    index = 0

    while index < len(inventory):

        item = inventory[index]

        total += item["quantity"] * item["price"]

        index += 1

    print(f"\nTotal inventory value: ${total:.2f}")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    inventory = load_inventory()

    choice = ""

    while choice != "7":

        print("\n")
        print("=" * 40)
        print("       INVENTORY MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. Display Inventory")
        print("2. Add Item")
        print("3. Search Item")
        print("4. Update Item")
        print("5. Remove Item")
        print("6. Calculate Inventory Value")
        print("7. Exit")
        print("=" * 40)

        choice = input("Enter your choice: ")

        if choice == "1":

            display_inventory(inventory)

        elif choice == "2":

            add_item(inventory)

        elif choice == "3":

            search_item(inventory)

        elif choice == "4":

            update_item(inventory)

        elif choice == "5":

            remove_item(inventory)

        elif choice == "6":

            calculate_inventory_value(inventory)

        elif choice == "7":

            save_inventory(inventory)

            print("\nInventory saved.")
            print("Goodbye!")

        else:

            print("\nInvalid choice. Please try again.")


# ============================================================
# START PROGRAM
# ============================================================

main()