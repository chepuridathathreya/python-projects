import sqlite3
conn = sqlite3.connect('D:\\dattu\\python projects\\PasswordManager\\passwords.db')
cursor = conn.cursor()
def main():
    print("Welcome to Password Manager")
    print("1. Add a password")
    print("2. View passwords")
    print("3. Search passwords")
    print("4. delete passwords")
    print("5. Exit")
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            website = input("enter website name: ")
            username = input("enter username: ")
            password = input("enter password: ")
            cursor.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)", (website, username, password))
            conn.commit()
        elif choice == '2':
            passw = cursor.execute("SELECT * FROM passwords")
            passw = passw.fetchall()
            for i in passw:
                print(i[0], i[1], i[2], i[3])    
        elif choice == '3':
            search = input("Enter website name to search: ")
            passw = cursor.execute("SELECT * FROM passwords WHERE website=?", (search,))
            passw = passw.fetchall()
            for i in passw:
                print(i[0], i[1], i[2], i[3])
        elif choice == '4':
            delete = input("Enter website name to delete: ")
            cursor.execute("DELETE FROM passwords WHERE website=?", (delete,))
            conn.commit()
        elif choice == '5':
            break
    conn.close()    