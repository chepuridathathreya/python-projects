print("Welcome to your notes dashboard!")
print("1. type 'add note' to add a new note")
print("2. type 'show notes' to see all your notes")
print("3. type 'clear notes' to clear all your notes")
print("4. type 'count notes' to count the number of notes you have")
print("5. type 'find item' to find a specific note")
print("6. type 'exit' to exit the notes dashboard")
while True:
        a = input("enter ur choice: ")    
        if a == "1":
            with open("NotesApp/mainfile.txt", "a") as file:
                print("Note added!")
                file.write(a + "\n")
        
        elif a == "2":
            with open("NotesApp/mainfile.txt", "r") as readfile:
                print("you have written:")
                print(readfile.read())
        elif a == "3":
            with open("NotesApp/mainfile.txt", "w") as file:
                print("Notes cleared!")  
        elif a == "4":
            with open("NotesApp/mainfile.txt", "r") as readnotes:
                notes = readnotes.readlines()
                print(f"You have {len(notes)} notes.")
        elif a == "5":
            f = input("enter the word to find : ")
            with open("NotesApp/mainfile.txt", "r") as finditem:
                items = finditem.readlines()
                found = False
                for item in items:
                    if f in item:
                        print(f"Found: {item.strip()}")
                        found = True
                if not found:
                    print("Item not found.")

        
        else:
            if a == "6":
                break
