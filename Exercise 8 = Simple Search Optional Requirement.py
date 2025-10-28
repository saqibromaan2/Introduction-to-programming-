def main():
    names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

    # Allow the user to input the search term
    search_name = input("Enter the name you want to search for: ")

    # Check if the entered name is in the list
    if search_name in names:
        print(f"{search_name} was found in the list!")
    else:
        print(f"{search_name} was NOT found in the list.")

if __name__ == "__main__":
    main()
