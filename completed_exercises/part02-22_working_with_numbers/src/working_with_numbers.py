print("Please type in integer numbers. Type in 0 to finish.")
numbers = 0
sum = 0
positives = 0

while True:
    number = int(input("Number: "))
    if number == 0:
        break
    elif number > 0:
        positives += 1

    sum += number 
    numbers += 1

print(f"Numbers typed in {numbers}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum / numbers}")
print(f"Positive numbers {positives}")
print(f"Negative numbers {numbers - positives}")