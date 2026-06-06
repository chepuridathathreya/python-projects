print("Welcome to the note taker!")
print("Type 'show notes' to see your notes, and 'exit' to quit.")
file = open("fileproject/file.txt", "a")
while True:
    a = input("Write something: ")
    
    if a == "show notes":
        readfile = open("fileproject/file.txt", "r")
        print("you have written:")
        print(readfile.read())
        readfile.close()
    elif a == "exit":
        break     
    else:
        file.write(a + "\n")
file.close()    
