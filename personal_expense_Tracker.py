expenses = []

with open("expenses.txt", "r")as file:

    for line in file:
        parts = line.strip().split(",")

        expense = {
            "price": float(parts[0]),
            "category": parts[1],
            "description": parts[2],
            "date": parts[3]
    }
        expenses.append(expense)


def add_expenses():
    while True:
        try:
            price = float(input("Enter amount: "))
            if price > 0:
                break
            print("Amount must be greater than 0!")
        except ValueError:
            print("Please Enter vailid number!")

    while True:   
        category = input("Enter category: ")
        if category.strip() != "":
            break
        print("Category cannot be empty!")

    while True:
        description = input("Enter description: ")
        if description.strip() != "":
            break
        print("Description not be empty!")

    while True:
        date = input("Enter date: ")
        if date.strip() != "":
            break
        print("Date not be empty!")

    expense = {
        "price": price,
        "category": category.strip(),
        "description": description.strip(),
        "date": date.strip()
            }
    
    expenses.append(expense)
    
    with open("expenses.txt", "a") as file:
        file.write(
            f"{expense['price']},{expense['category']},{expense['description']}, {expense['date']}\n"
            )
    
    print("Expense Added Successfully! ")

def view_expenses():
    if len(expenses) == 0:
        print("No expenses available!")
        return

    number = 1

    for expense in expenses:
        print("\nExpense", number)
        print("Price:", expense["price"])
        print("Category:", expense["category"])
        print("Description:", expense["description"])
        print("Date:", expense["date"])
        print("--------------------")

        number += 1

def total_expenses():
    total = 0
    for expense in expenses:
        total += expense["price"]

    return total

def delete_expenses():
        if  len(expenses) == 0:
            print("No expense available!")
            return
            
        number = 1

        for expense in expenses:
            print(number, ".", expense["price"], "-", expense["category"], "-", expense["description"] )
            number += 1

        try:
            choice = int(input("Enter expense number to delete:"))

            if choice <=0:    
                print("Choise must be greter than zero")
                return  

            if choice > len(expenses):
                print("Invailid expense number!")
                return

            index = choice - 1

            expenses.pop(index)

            save_expenses()
            print("Expense delete successfully!")
        except ValueError:
            print("please enter a vailid number!")

def edit_expenses():
        if len(expenses) == 0:
            print("No expense available!")

        number = 1  

        for expense in expenses:
            print(number, ".", expense["price"], "-", expense["category"], "-", expense["description"] )
            number += 1

        try:
            choice = int(input("Enter expense number to edit:"))
            if choice <= 0 or choice > len(expenses):
                print("Invalid expense number!")
                return

            index = choice - 1 

            new_price = float(input("Enter new price:"))
            if new_price <= 0:
                print("Price must be grater than zero!")
                return
            new_category = input("Enter new category:")
            new_description = input("Enter new descriptioin:")
            new_date = input("Enter date: ")

            if new_category == "":
                print("Category cannot be empty!")
                return

            if new_description == "":
                print("Description cannot be empty!")
                return

            if new_date == "":
                print("Date cannot be empty!")
                return
            
            expenses[index]["price"]= new_price
            expenses[index]["category"]= new_category
            expenses[index]["description"]= new_description
            expenses[index]["date"]= new_date

            save_expenses()

            print("Expense Edit Successfully!")

        except ValueError:
            print("Please Enter vailid number!")

def search_expenses():
    search = input("Enter category to search: ")

    found = False

    for expense in expenses:
        if expense["category"].lower() == search.lower():
            print("Price:", expense["price"])
            print("Category:", expense["category"])
            print("Description:", expense["description"])
            print("Date:", expense["date"])
            print("--------------------")
            found = True

    if not found:
        print("No expense found!")

def category_summary():

    if len(expenses) == 0:
        print("No expenses available!")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        price = expense["price"]

        if category in categories:
            categories[category] += price
        else:
            categories[category] = price

    for category in categories:
        print(category, ":", categories[category])

def monthly_summary():

    if len(expenses) == 0:
        print("No expenses available!")
        return
    
    month = input("Enter month (01-12): ").strip().zfill(2)

    total = 0
    found = False

    for expense in expenses:
        date = expense["date"]

        expense_month = date.split("-")[1].strip().zfill(2)

        if expense_month == month:
            total += expense["price"]
            found = True

    if found:
        print("Total expenses for month:", total)
    else:
        print("No expenses found for this month!")

def save_expenses():

    with open("expenses.txt", "w") as file:

        for expense in expenses:

            file.write(
                f"{expense['price']},{expense['category']},"
                f"{expense['description']},{expense['date']}\n"
            )

while True:
    print("\n====== EXPENSE TRACKER ======")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Show Total Expenses")
    print("4. Delete Expenses")
    print("5. Edit Expenses")
    print("6. Search Expenses")
    print("7. Category Summery")
    print("8. Monthly Summery")
    print("9. Exit")
    print("=" *30)

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number!")
        continue

    if choice not in [1,2,3,4,5,6,7,8,9]:
        print("Invalid choice! Please choose 1 to 4.")
        continue

    if choice == 1:
       add_expenses()

    elif choice == 2:
        view_expenses()

    elif choice == 3:
        total = total_expenses()
        print(f"Total Expense: {total}")

    elif choice == 4:
        delete_expenses()

    elif choice == 5:
        edit_expenses()

    elif choice == 6:
        search_expenses()

    elif choice == 7:
        category_summary()

    elif choice == 8:
        monthly_summary()
    elif choice == 9:
        print("Exit succesfully!")
        break

    else:
        print("Invalid choice! Please choose 1 to 9.")