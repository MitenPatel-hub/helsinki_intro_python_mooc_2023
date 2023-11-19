limit = int(input("Limit: "))
number = 1
counter_string = "1"
sum = 1

while sum < limit:
    number += 1
    counter_string += f" + {number}"
    sum += number

print(f"The consecutive sum: {counter_string} = {sum}")