import sqlite3
import os
from datetime import date, datetime
date = datetime.now()
connection = sqlite3.connect("assistent.db")
cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())
while True:
    print("welcome to personal assistant")
    print("type 1 for Notes")
    print("type 2 for Expenses")
    print("type 3 for Passwords")
    print("type 4 for search")
    print("5 for exit")
    main_choice = int(input("ENTER YOUR CHOICE: "))
    if main_choice == 1:
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
                cursor.execute("INSERT INTO notes (note, created_date) VALUES (?, ?)", (note, date.strftime("%Y-%m-%d %H:%M")))
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
