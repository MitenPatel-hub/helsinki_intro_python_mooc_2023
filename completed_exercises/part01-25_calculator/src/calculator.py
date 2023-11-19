'''
# Solution 1
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ")
add = operation == "add"
subtract = operation == "subtract"
multiply = operation == "multiply"

if add:
  result = number1 + number2
  print(f"{number1} + {number2} = {result}")

if subtract:
  result = number1 - number2
  print(f"{number1} - {number2} = {result}")

if multiply:
  result = number1 * number2
  print(f"{number1} * {number2} = {result}")

# Solution 2
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ")
add = operation == "add"
subtract = operation == "subtract"
multiply = operation == "multiply"

if add:
  result = number1 + number2
  print(number1, "+", number2, "=", result)

if subtract:
  result = number1 - number2
  print(number1, "-", number2, "=", result)

if multiply:
  result = number1 * number2
  print(number1, "*", number2, "=", result)

# Solution 3
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ")

if operation == "add":
  result = number1 + number2
  print(number1, "+", number2, "=", result)

if operation == "subtract":
  result = number1 - number2
  print(number1, "-", number2, "=", result)

if operation == "multiply":
  result = number1 * number2
  print(number1, "*", number2, "=", result)

'''

# Solution 4

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ")

if operation == "add":
  print(number1, "+", number2, "=", number1 + number2)

if operation == "subtract":
  print(number1, "-", number2, "=", number1 - number2)

if operation == "multiply":
  print(number1, "*", number2, "=", number1 * number2)