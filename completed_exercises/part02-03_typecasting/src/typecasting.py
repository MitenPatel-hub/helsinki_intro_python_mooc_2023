'''
# Solution 1
number = float(input("Please type in a number: "))
print(f"Integer part: {int(number)}")
print(f"Decimal part: {number - (int(number))}")
'''

# Solution 2
number = float(input("Please type in a number: "))
integer_part = int(number)
decimal_part = number - integer_part
print(f"Integer part: {integer_part}")
print(f"Decimal part: {decimal_part}")