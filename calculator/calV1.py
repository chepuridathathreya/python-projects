#OK SO A SIMPLE CALCULATOR IN PYTHON USING JUST NORMAL BASICS MOST OF THE TOPICS COVERS IN HERE
print("WELCOME")
print("1 for addition ")
print("2 for subtraction ")
print("3 for multiplication ")
print("4 for division ")
print("5 for percentage")
print("Type 'exit' to quit the calculator.")
while True:
    opt = (input("Enter the option: "))
    if opt in ["1","2","3","4"]:
        try :
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            
            if opt == "1":
                print("The sum is: ", a + b)
            elif opt == "2":
                print("The difference is: ", a - b)
            elif opt == "3":
                print("The product is: ", a * b)
            elif opt == "4":
                if b != 0:
                    print("The quotient is: ", a / b)
                else:
                    print("Error: Division by zero is not allowed.")           
        except ValueError:
            print("Invalid input. Please enter numeric values.")            
    elif opt == "5":
        try:
            a = float(input("Enter the number: "))
            b = float(input("Enter the percentage: "))
            print(f"{b}% of {a} is: ", (a * b) / 100)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    elif opt == "exit":
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")

        