# Solution 1
input_string = input("Please type in a string: ")
index = -1

while index >= -len(input_string):
    print(input_string[index])
    index -= 1

'''
# Solution 2
input_string = input("Please type in a string: ")
index = 1

while index <= len(input_string):
    print(input_string[-index])
    index += 1

# Solution 3
input_string = input("Please type in a string: ")
index = 1

while index <= len(input_string):
    print(input_string[len(input_string)-index])
    index += 1
'''