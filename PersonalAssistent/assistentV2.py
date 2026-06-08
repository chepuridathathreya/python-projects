import sqlite3
from datetime import date, datetime
current_date = datetime.now()
connection = sqlite3.connect("assisV2.db")
cursor = connection.cursor()


def notes():

    print("welcome to Notes")
    print("type 1 for add notes")
    print("type 2 for view notes")
    print("type 3 for delete notes")
    print("type 4 for search notes")
    print("type 5 for exit")
    while True:
                notes_choice = int(input("ENTER YOUR CHOICE: "))
                if notes_choice == 1:
                    note = input("enter your note: ")
                    cursor.execute("INSERT INTO notes (note, created_date) VALUES (?, ?)", (note, current_date.strftime("%Y-%m-%d %H:%M")))
                    connection.commit()
                    print("note added successfully")
                elif notes_choice == 2:
                    cursor.execute("SELECT * FROM notes")
                    notes = cursor.fetchall()
                    for note in notes:
                        print(f"ID: {note[0]}, Note: {note[1]}, Created Date: {note[2]}")
                elif notes_choice == 3:
                    note_id = int(input("enter the id of the note you want to delete: "))
                    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
                    connection.commit()
                    print("note deleted successfully")    
                elif notes_choice == 4:
                        search_word = input("Enter word to search: ")
                        cursor.execute("SELECT * FROM notes WHERE note LIKE ?",
                            ('%' + search_word + '%',))

                        results = cursor.fetchall()

                        if len(results) == 0:
                            print("No notes found.")

                        else:
                            for note in results:
                                print(
                                    f"ID: {note[0]}, "
                                    f"Note: {note[1]}, "
                                    f"Created Date: {note[2]}"
                                )
                else:
                    print("exiting notes")
                    break       
def expenses():

    print("welcome to Expenses")

    print("type 1 for add expenses")
    print("type 2 for view expenses")
    print("type 3 for delete expenses")
    print("type 4 for search expenses")
    print("type 5 for exit")
    while True:
            expenses_choice = int(input("ENTER YOUR CHOICE: "))
            if expenses_choice == 1:
                amount = float(input("enter the amount: "))
                category = input("enter the category: ")
                cursor.execute("INSERT INTO expenses (amount, category, created_date) VALUES (?, ?, ?)", (amount, category, current_date.strftime("%Y-%m-%d %H:%M")))
                connection.commit()
                print("expense added successfully")
            elif expenses_choice == 2:
                cursor.execute("SELECT * FROM expenses")
                expenses = cursor.fetchall()
                for expense in expenses:
                    print(f"ID: {expense[0]}, Amount: {expense[1]}, Category: {expense[2]}, Created Date: {expense[3]}")
            elif expenses_choice == 3:
                expense_id = int(input("enter the id of the expense you want to delete: "))
                cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
                connection.commit()
                print("expense deleted successfully")    
            elif expenses_choice == 4:
                    search_word = input("Enter word to search: ")
                    cursor.execute("SELECT * FROM expenses WHERE category LIKE ?",
                        ('%' + search_word + '%',))

                    results = cursor.fetchall()

                    if len(results) == 0:
                        print("No expenses found.")

                    else:
                        for expense in results:
                            print(
                                f"ID: {expense[0]}, "
                                f"Amount: {expense[1]}, "
                                f"Category: {expense[2]}, "
                                f"Created Date: {expense[3]}"
                            )
            else:
                print("exiting expenses")
                break  
def password_manager():

    print("welcome to Password Manager")

    print("type 1 for add password")
    print("type 2 for view passwords")
    print("type 3 for delete passwords")
    print("type 4 for search passwords")
    print("type 5 for exit")
    while True:
            password_choice = int(input("ENTER YOUR CHOICE: "))
            if password_choice == 1:
                website = input("enter the website: ")
                username = input("enter the username: ")
                password = input("enter the password: ")
                cursor.execute("INSERT INTO passwords (website, username, password, created_date) VALUES (?, ?, ?, ?)", (website, username, password, current_date.strftime("%Y-%m-%d %H:%M")))
                connection.commit()
                print("password added successfully")
            elif password_choice == 2:
                cursor.execute("SELECT * FROM passwords")
                passwords = cursor.fetchall()
                for password in passwords:
                    print(f"ID: {password[0]}, Website: {password[1]}, Username: {password[2]}, Password: {password[3]}, Created Date: {password[4]}")
            elif password_choice == 3:
                password_id = int(input("enter the id of the password you want to delete: "))
                cursor.execute("DELETE FROM passwords WHERE id = ?", (password_id,))
                connection.commit()
                print("password deleted successfully")    
            elif password_choice == 4:
                    search_word = input("Enter word to search: ")
                    cursor.execute("SELECT * FROM passwords WHERE website LIKE ?",
                        ('%' + search_word + '%',))

                    results = cursor.fetchall()

                    if len(results) == 0:
                        print("No passwords found.")

                    else:
                        for password in results:
                            print(
                                f"ID: {password[0]}, "
                                f"Website: {password[1]}, "
                                f"Username: {password[2]}, "
                                f"Password: {password[3]}, "
                                f"Created Date: {password[4]}"
                            )
            else:
                print("exiting password manager")
                break            
def global_serch():
             
            search_word = input("Enter word to search: ")
            cursor.execute("SELECT * FROM notes WHERE note LIKE ?",
                ('%' + search_word + '%',))

            notes_results = cursor.fetchall()

            cursor.execute("SELECT * FROM expenses WHERE category LIKE ?",
            ('%' + search_word + '%',))

            expenses_results = cursor.fetchall()

            cursor.execute("SELECT * FROM passwords WHERE website LIKE ?",
            ('%' + search_word + '%',))

            passwords_results = cursor.fetchall()

            if len(notes_results) == 0 and len(expenses_results) == 0 and len(passwords_results) == 0:
                print("No results found.")

            else:
                for note in notes_results:
                    print(
                        f"ID: {note[0]}, "
                        f"Note: {note[1]}, "
                        f"Created Date: {note[2]}"
                    )

            for expense in expenses_results:
                print(
                    f"ID: {expense[0]}, "
                    f"Amount: {expense[1]}, "
                    f"Category: {expense[2]}, "
                    f"Created Date: {expense[3]}"
                )

            for password in passwords_results:
                print(
                    f"ID: {password[0]}, "
                    f"Website: {password[1]}, "
                    f"Username: {password[2]}, "
                    f"Password: {password[3]}, "
                    f"Created Date: {password[4]}"
                )
print("welcome to Personal Assistant")
print("type 1 for Notes")
print("type 2 for Expenses")
print("type 3 for Password Manager")
print("type 4 for Global Search")
print("type 5 for analysis")
print("type 6 for exit")
while True:
    main_choice = int(input("ENTER YOUR CHOICE: "))
    if main_choice == 1:
        notes()
    elif main_choice == 2:
        expenses()
    elif main_choice == 3:
        password_manager()
    elif main_choice == 4:
        global_serch()
    elif main_choice == 5:
        print("==================")
        print("PERSONAL ANALYSIS")
        print("==================")
        cursor.execute("SELECT COUNT(*) FROM notes")
        note_count = cursor.fetchone()[0]
        print(f"Total Notes: {note_count}")
        cursor.execute("SELECT COUNT(*) FROM expenses")
        expense_count = cursor.fetchone()[0]
        print(f"Total Expenses: {expense_count}")
        cursor.execute("SELECT COUNT(*) FROM passwords")
        password_count = cursor.fetchone()[0]
        print(f"Total Passwords: {password_count}")
    else:
        print("exiting Personal Assistant")
        break                  
                