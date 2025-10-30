# Function to check if a number is even or odd
def is_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Main function
def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))
    
    # Call the function and get the result
    result = is_even_or_odd(num)
    
    # Print the result
    print(result)

# Run the program
if __name__ == "__main__":
    main()
