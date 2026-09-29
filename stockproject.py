
# CSE1021 - Stock Tracker
# A simple program to manage a stock portfolio.

portfolio = {}


def add_stock(portfolio):
    print("\n--- ADD STOCK ---")

    stock_name = input("Enter stock name: ").upper().strip()

    if stock_name == "":
        print("Stock name cannot be blank.")
        return

    if stock_name in portfolio:
        print("This stock is already in your portfolio.")
        return

    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per share: "))
    except ValueError:
        print("Please enter valid numbers for quantity and price.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    if price <= 0:
        print("Price must be greater than zero.")
        return

    # Store quantity and price in a list inside the dictionary.
    portfolio[stock_name] = [quantity, price]

    print("Stock added successfully.")


def view_stocks(portfolio):
    print("\n--- YOUR STOCKS ---")

    if len(portfolio) == 0:
        print("Your portfolio is empty.")
        return

    for stock_name in portfolio:
        quantity = portfolio[stock_name][0]
        price = portfolio[stock_name][1]

        total_value = quantity * price

        print("\nStock:", stock_name)
        print("Quantity:", quantity)
        print("Price per share:", price)
        print("Total value:", total_value)


def calculate_total(portfolio):
    total = 0

    for stock_name in portfolio:
        quantity = portfolio[stock_name][0]
        price = portfolio[stock_name][1]

        total = total + (quantity * price)

    print("\nTotal money invested:", total)


def search_stock(portfolio):
    print("\n--- SEARCH STOCK ---")

    stock_name = input("Enter stock name to search: ").upper().strip()

    if stock_name in portfolio:
        quantity = portfolio[stock_name][0]
        price = portfolio[stock_name][1]

        total_value = quantity * price

        print("\nStock found!")
        print("Stock:", stock_name)
        print("Quantity:", quantity)
        print("Price per share:", price)
        print("Total value:", total_value)

    else:
        print("Stock was not found in your portfolio.")


def highest_investment(portfolio):
    if len(portfolio) == 0:
        print("\nYour portfolio is empty.")
        return

    highest_value = -1
    highest_stock = ""

    for stock_name in portfolio:
        quantity = portfolio[stock_name][0]
        price = portfolio[stock_name][1]

        total_value = quantity * price

        if total_value > highest_value:
            highest_value = total_value
            highest_stock = stock_name

    print("\n--- HIGHEST INVESTMENT ---")
    print("Stock:", highest_stock)
    print("Investment value:", highest_value)


def delete_stock(portfolio):
    print("\n--- DELETE STOCK ---")

    stock_name = input("Enter stock name to delete: ").upper().strip()

    if stock_name in portfolio:
        del portfolio[stock_name]
        print("Stock deleted successfully.")
    else:
        print("Stock was not found in your portfolio.")


# Main program
running = True

while running:
    print("\n==============================")
    print("       STOCK TRACKER")
    print("==============================")
    print("1. Add stock")
    print("2. View all stocks")
    print("3. Calculate total investment")
    print("4. Search for a stock")
    print("5. Find highest investment")
    print("6. Delete a stock")
    print("7. Exit")
    print("==============================")

    choice = input("Enter your choice (1-7): ").strip()

    if choice == "1":
        add_stock(portfolio)

    elif choice == "2":
        view_stocks(portfolio)

    elif choice == "3":
        calculate_total(portfolio)

    elif choice == "4":
        search_stock(portfolio)

    elif choice == "5":
        highest_investment(portfolio)

    elif choice == "6":
        delete_stock(portfolio)

    elif choice == "7":
        print("\nThank you for using Stock Tracker. Goodbye!")
        running = False

    else:
        print("\nInvalid choice. Please enter a number from 1 to 7.")
