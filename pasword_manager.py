passwords = {}

def add_password():
    website = input("Enter website name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    passwords[website] = {"username": username, "password": password}
    print("Password added successfully!")

def get_password():
    website = input("Enter website name: ")
    if website in passwords:
        username = passwords[website]["username"]
        password = passwords[website]["password"]
        print("Username:", username)
        print("Password:", password)
    else:
        print("Website not found!")

def main():
    while True:
        print("\n--- Password Manager ---")
        print("1. Add password")
        print("2. Get password")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_password()
        elif choice == '2':
            get_password()
        elif choice == '3':
            break
        else:
            print("Invalid choice!")

if __name__ == '__main__':
    main()
