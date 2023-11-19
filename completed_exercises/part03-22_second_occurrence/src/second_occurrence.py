# Solution 1
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
index = string.find(substring)
next_index = string.find(substring, index + len(substring))

if next_index != -1:
    print(f"The second occurrence of the substring is at index {next_index}.")
else:
    print("The substring does not occur twice in the string.")

'''
# Solution 2
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
index = string.find(substring)

if index == -1:
    print("The substring does not occur twice in the string.")
else:
    index = string.find(substring, index + len(substring))
    if index != -1:
        print(f"The second occurrence of the substring is at index {index}.")
    else:
        print("The substring does not occur twice in the string.")

# Solution 3
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
index = string.find(substring)

if index == -1:
    print("The substring does not occur twice in the string.")
elif len(string) > len(substring) * 2:
    index += len(substring)
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            print(f"The second occurrence of the substring is at index {index}.")
            break
        index += 1
else:
    print("The substring does not occur twice in the string.")
'''