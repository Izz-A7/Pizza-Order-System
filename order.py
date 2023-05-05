# Used to make code in "pizzaReceipt" available in "order".
from pizzaReceipt import *

# Define list of toppings.
TOPPINGS = (
    "ONION",
    "TOMATO",
    "GREEN PEPPER",
    "MUSHROOM",
    "OLIVE",
    "SPINACH",
    "BROCCOLI",
    "PINEAPPLE",
    "HOT PEPPER",
    "PEPPERONI",
    "HAM",
    "BACON",
    "GROUND BEEF",
    "CHICKEN",
    "SAUSAGE"
)

# Define the user's list of orders.
orderList = []
# Capture user input on if they would like to order a pizza.
pizzaOrder = input("Do you want to order a pizza? ")

while True:
    # Terminate loop if 'NO' or 'Q' are entered.
    pizzaOrder = pizzaOrder.upper()
    if ("NO" == pizzaOrder) or ("Q" == pizzaOrder):
        break

    # Iterate over the user input to create order list.
    successfulOrder = False
    # Capture user input on size.
    while not successfulOrder:
        size = input("Choose a size: S, M, L, or XL: ")
        size = size.upper()

        # If user does not input any valid sizes, previous input will repeat.
        if ("S" != size.upper()) and ("M" != size.upper()) and ("L" != size.upper()) and ("XL" != size.upper()):
            continue

        # Define the user's list of toppings.
        toppings = []
        # Capture user input on toppings.
        while True:
            topping = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"\n")
            topping = topping.upper()

            # Exit toppings if user inputs "X".
            if "X" == topping.upper():
                successfulOrder = True
                orderList.append((size, toppings))
                break
            # Output list of toppings if user inputs "LIST".
            elif "LIST" == topping:
                print(TOPPINGS)
            # If user inputs a topping that is available in the toppings list, add the topping into the user's toppings list.
            elif topping in TOPPINGS:
                toppings.append(topping)

    # Capture user input on whether they would like to order another pizza or finish the order.
    pizzaOrder = input("Do you want to continue ordering? ")

# Run the generateReceipt function to print results.
generateReceipt(orderList)
