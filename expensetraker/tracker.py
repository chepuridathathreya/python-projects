print("welcome to expense tracker")
print ("what do you want to do?" )
print("1. add expense")
print("2. view expenses")
print("3. view total expenses")
print("4. search by category")
print("'done' to exit")
while True:
    choice = input("enter your choice: ")
    if choice not in ['1', '2', '3', '4', 'done']:
        print("invalid choice, please try again.")
        continue
    elif choice == '1':
        amount = float(input("enter the amount: "))
        category = input("enter the category: ")
        with open("expenses.txt", "a") as file:
            file.write(f"{amount} - {category}\n")
        print("expense added successfully!")
    elif choice == '2':
        print("your expenses:")
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
            for expense in expenses:
                print(expense.strip())
    elif choice == '3':
        total = 0
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
            for expense in expenses:
                amount = float(expense.split(" - ")[0])
                total += amount
        print(f"total expenses: {total}")      
    elif choice == '4':     
        search_category = input("enter the category to search: ")
        print(f"expenses in category '{search_category}':")
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
            found = False
            for expense in expenses:
                if search_category in expense:
                    print(expense.strip())
                    found = True
            if not found:
                print("no expenses found in this category.")     
    elif choice == 'done':
        print("exiting the expense tracker. Goodbye!")
        break