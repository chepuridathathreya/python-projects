print("Welcome to the note taker!")
print("Type 'show notes' to see your notes, 'clear notes' to clear them, and 'exit' to quit.")
while True:
    a = input("Write something: ")    
    if a == "show notes":
        with open("fileproject/nfile.txt", "r") as readfile:
            print("you have written:")
            print(readfile.read())
    elif a == "clear notes":
        with open("fileproject/nfile.txt", "w") as file:
            print("Notes cleared!")  
    elif a == "count notes":
        with open("fileproject/nfile.txt", "r") as readnotes:
            notes = readnotes.readlines()
            print(f"You have {len(notes)} notes.")
    elif a == "find item":
        f = input("enter the word to find : ")
        with open("fileproject/nfile.txt", "r") as finditem:
            items = finditem.readlines()
            found = False
            for item in items:
                if f in item:
                    print(f"Found: {item.strip()}")
                    found = True
            if not found:
                print("Item not found.")

    elif a == "exit":
        break     
    else:
        with open("fileproject/nfile.txt", "a") as file:
            print("Note added!")
            file.write(a + "\n")
        