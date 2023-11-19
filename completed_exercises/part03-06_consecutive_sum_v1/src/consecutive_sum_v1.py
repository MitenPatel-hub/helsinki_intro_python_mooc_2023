limit = int(input("Limit: "))
number = 1
following_number = number + 1
sum = number + following_number

while sum < limit:
    following_number += 1
    sum += following_number

print(sum)