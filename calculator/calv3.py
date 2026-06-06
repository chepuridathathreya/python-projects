def history(num1,num2,operation,result):
    my_histiory = open("calculator/history.txt", "a")
    my_histiory.write(f"{num1} {operation} {num2} = {result}\n")
    my_histiory.close()
def cal(opt, a, b):
    if opt in ["1","2","3","4","5"]:
            if opt == "1":
                print("The sum is: ", a + b)    
                sum_result = a + b
                history(a,b,"+",sum_result)
            elif opt == "2":
                print("The difference is: ", a - b)
                diff_result = a - b
                history(a,b,"-",diff_result)        
            elif opt == "3":
                print("The product is: ", a * b)
                product_result = a * b
                history(a,b,"*",product_result)
            elif opt == "4":
                if b != 0:
                    print("The quotient is: ", a / b)
                    quotient_result = a / b
                    history(a,b,"/",quotient_result)
                else:
                    print("Error: Division by zero is not allowed.")
            elif opt == "5":
                print(f"{b}% of {a} is: ", (a * b) / 100)



print("WELCOME")
print("1 for addition ")
print("2 for subtraction ")
print("3 for multiplication ")
print("4 for division ")
print("5 for percentage")
print("6 for history")
print("Type 'exit' to quit the calculator.")
while True:
    opt = (input("Enter the option: "))
    if opt in ["1","2","3","4"]:  
        try :
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            cal(opt, a, b)
        except ValueError:
                print("Invalid input. Please enter numeric values.")    
    elif opt == "5":
        try:
            a = float(input("Enter the number: "))
            b = float(input("Enter the percentage: "))
            cal(opt, a, b)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    elif opt == "6":
        my_history = open("calculator/history.txt", "r")
        print("History of calculations:")
        print(my_history.read())
        my_history.close()

    elif opt == "exit":
        print("Exiting the calculator. Goodbye!")
        break   
    else:
         print("Invalid option. Please try again.")         