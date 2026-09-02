# Online Shopping Cart System

cart = []

while True:

    print("\n===== SHOPPING CART =====")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Change Quantity")
    print("4. Display Bill")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Add Product
    if choice == 1:
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        cart.append([name, price, quantity])

        print("Product added!")

    # Remove Product
    elif choice == 2:
        name = input("Enter product name to remove: ")

        for product in cart:
            if product[0] == name:
                cart.remove(product)
                print("Product removed!")
                break
        else:
            print("Product not found!")

    # Change Quantity
    elif choice == 3:
        name = input("Enter product name: ")
        quantity = int(input("Enter new quantity: "))

        for product in cart:
            if product[0] == name:
                product[2] = quantity
                print("Quantity changed!")
                break
        else:
            print("Product not found!")

    # Display Bill
    elif choice == 4:

        subtotal = 0

        print("\n========== BILL ==========")

        for product in cart:
            total = product[1] * product[2]

            print(product[0], "-", product[1], "x", product[2], "=", total)

            subtotal = subtotal + total

        print("--------------------------")
        print("Subtotal:", subtotal)

        discount_percent = float(input("Enter discount %: "))
        discount = subtotal * discount_percent / 100

        amount = subtotal - discount

        gst_percent = float(input("Enter GST %: "))
        gst = amount * gst_percent / 100

        final_amount = amount + gst

        print("Discount:", discount)
        print("GST:", gst)
        print("Final Amount:", final_amount)

    # Exit
    elif choice == 5:
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice!")