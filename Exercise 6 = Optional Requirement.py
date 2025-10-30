def main():
    correct_password = "12345"
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        password = input("Enter the password: ")
        if password == correct_password:
            print("Access granted.")
            break
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Incorrect password. You have {remaining} attempt(s) left.")
            else:
                print("Maximum attempts reached. Authorities have been alerted.")

if __name__ == "__main__":
    main()
