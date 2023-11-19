left = 1
number = int(input("Please type in a number: "))

while left <= number:
    right = 1
    while right <= number:
        print(f"{left} x {right} = {left * right}")
        right += 1
    left += 1
