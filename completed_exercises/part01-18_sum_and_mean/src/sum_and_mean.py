# Solution 1

total = 0

total += int(input("Number 1: "))
total += int(input("Number 2: "))
total += int(input("Number 3: "))
total += int(input("Number 4: "))

print(f"The sum of the numbers is {total} and the mean is {total / 4 }")

'''
# Solution 2

sum = 0
number_of_inputs = 0

sum += int(input("Number 1: "))
number_of_inputs+=1

sum += int(input("Number 2: "))
number_of_inputs+=1

sum += int(input("Number 3: "))
number_of_inputs+=1

sum += int(input("Number 4: "))
number_of_inputs+=1

mean = sum / number_of_inputs

print(f"The sum of the numbers is {sum} and the mean is {mean}")


# Solution 3

sum = 0
number_of_inputs = 0

sum += int(input(f"Number {number_of_inputs + 1}: "))
number_of_inputs+=1

sum += int(input(f"Number {number_of_inputs + 1}: "))
number_of_inputs+=1

sum += int(input(f"Number {number_of_inputs + 1}: "))
number_of_inputs+=1

sum += int(input(f"Number {number_of_inputs + 1}: "))
number_of_inputs+=1

mean = sum / number_of_inputs

print(f"The sum of the numbers is {sum} and the mean is {mean}")

Solution 4:

sum = 0
number_of_inputs = 0

for _ in range(4):  
    sum += int(input(f"Number {number_of_inputs+1}: "))
    number_of_inputs += 1

mean = sum / number_of_inputs

print(f"The sum of the numbers is {sum} and the mean is {mean}")
'''
