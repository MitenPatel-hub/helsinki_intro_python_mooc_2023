while True:
    number = int(input("Please type in a number: "))
    factorial = 1
    if number > 0:
        counter = number
        while counter > 0:
            factorial *= counter
            counter -= 1
        print(f"The factorial of the number {number} is {factorial}")
    else:
        break
        
print("Thanks and bye!")