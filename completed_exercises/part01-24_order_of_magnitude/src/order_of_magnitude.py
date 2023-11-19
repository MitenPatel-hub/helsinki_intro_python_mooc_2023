# Get user input
number = int(input("Please type in a number: "))

# Check if the number is smaller than 1000
if number < 1000:
    print("This number is smaller than 1000")

    # Check if the number is also smaller than 100
    if number < 100:
        print("This number is smaller than 100")

        # Check if the number is also smaller than 10
        if number < 10:
            print("This number is smaller than 10")

# Print thank you message
print("Thank you!")