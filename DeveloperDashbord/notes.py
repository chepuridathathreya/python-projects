def main():

    print("Welcome to your notes dashboard!")

    print("type 'add note' to add a new note")
    print("type 'show notes' to see all your notes")
    print("type 'clear notes' to clear all your notes")
    print("type 'count notes' to count the number of notes you have")
    print("type 'find item' to find a specific note")
    print("type 'exit' to exit the notes dashboard")
    while True:
        a = input("Write something: ")    
        if a == "show notes":
            with open("DeveloperDashbord/mainfile.txt", "r") as readfile:
                print("you have written:")
                print(readfile.read())
        elif a == "clear notes":
            with open("DeveloperDashbord/mainfile.txt", "w") as file:
                print("Notes cleared!")  
        elif a == "count notes":
            with open("DeveloperDashbord/mainfile.txt", "r") as readnotes:
                notes = readnotes.readlines()
                print(f"You have {len(notes)} notes.")
        elif a == "find item":
            f = input("enter the word to find : ")
            with open("DeveloperDashbord/mainfile.txt", "r") as finditem:
                items = finditem.readlines()
                found = False
                for item in items:
                    if f in item:
                        print(f"Found: {item.strip()}")
                        found = True
                if not found:
                    print("Item not found.")

        elif a == "add note":
            with open("DeveloperDashbord/mainfile.txt", "a") as file:
                print("Note added!")
                file.write(a + "\n")
        elif a == "exit":
            break     
            