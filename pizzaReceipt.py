# Define constants.
TAX_PERCENTAGE = 0.13
XL_PIZZA_COST = 13.99
XL_PIZZA_EXTRA_TOPPING_COST = 1.25
L_PIZZA_COST = 11.99
L_PIZZA_EXTRA_TOPPING_COST = 1
M_PIZZA_COST = 9.99
M_PIZZA_EXTRA_TOPPING_COST = 0.75
S_PIZZA_COST = 7.99
S_PIZZA_EXTRA_TOPPING_COST = 0.5
NUMBER_OF_FREE_TOPPINGS = 3

def generateReceipt(orderList):
    # Define bill.
    bill = 0

    # Check if orderList is empty.
    if not len(orderList):
        print("You did not order anything")
    else:
        print("Your order: ")

        # Iterate over orders in orderList.
        for i in range(0, len(orderList)):
            size = orderList[i][0]
            toppings = orderList[i][1]

            # Set pizza and extra toppings costs based on the sizes.
            pizzaCost = XL_PIZZA_COST
            toppingCost = XL_PIZZA_EXTRA_TOPPING_COST
            if "S" == size:
                pizzaCost = S_PIZZA_COST
                toppingCost = S_PIZZA_EXTRA_TOPPING_COST
            elif "M" == size:
                pizzaCost = M_PIZZA_COST
                toppingCost = M_PIZZA_EXTRA_TOPPING_COST
            elif "L" == size:
                pizzaCost = L_PIZZA_COST
                toppingCost = L_PIZZA_EXTRA_TOPPING_COST

            # Print pizza number and pizza cost correlating with size.
            print(f'Pizza {i+1}: {size}\t\t\t\t{pizzaCost:.2f}')

            # Print toppings.
            toppingsLength = len(toppings)
            for j in range(0, toppingsLength):
                print("- " + toppings[j])

            # Determine the number of extra toppings.
            extraToppings = 0
            if toppingsLength >= NUMBER_OF_FREE_TOPPINGS:
                extraToppings = toppingsLength - NUMBER_OF_FREE_TOPPINGS

            # Compute the cumulative order cost.
            bill += pizzaCost + extraToppings * toppingCost

            # Print extra topping cost for every extra topping.
            for j in range(0, extraToppings):
                print(f'Extra Topping ({size})\t\t{toppingCost:.2f}')

        # Print and compute tax rate.
        tax = bill * TAX_PERCENTAGE
        print(f'Tax:\t\t\t\t\t{tax:.2f}')
        # Print and compute total bill.
        print(f'Total:\t\t\t\t\t{bill + tax:.2f}')





