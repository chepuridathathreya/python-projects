import movie
import password
import notes
import expenses
if __name__ == "__main__":
    print("welcome to the DashBoard")
    print("1. Movie details")
    print("2. To take notes")
    print("3. To track expenses")
    print("4. To save ur passwords")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            movie.main()
        elif choice == 2:
            notes.main()
        elif choice == 3:
            expenses.main()
        elif choice == 4:    
            password.main()
        else:   
            print("Invalid choice, please try again.")     
    except ValueError:
        print("Invalid input, please enter a number corresponding to your choice.")        