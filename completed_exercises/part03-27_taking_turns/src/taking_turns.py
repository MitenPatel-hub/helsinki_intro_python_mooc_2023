number = int(input("Please type in a number: "))
left = 1
right = number
while left <= right:
    print(left)
    if left == right:
        break
    print(right)
    left += 1
    right -= 1
