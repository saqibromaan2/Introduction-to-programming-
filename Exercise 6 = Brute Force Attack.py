def main():
    correct_password = "12345"
    password = ""

    while password != correct_password:
        password = input("Enter the password: ")
        if password == correct_password:
            print("Access granted.")
        else:
            print("Incorrect password. Try again.")

if __name__ == "__main__":
    main()
