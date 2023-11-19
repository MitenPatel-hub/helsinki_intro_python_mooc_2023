string = input("Please type in a string: ")
start_index = -1
slice = string[-1]

while start_index >= -len(string):
    print(slice)
    previous = slice
    if start_index == -len(string):
        break
    start_index -= 1
    slice = string[start_index] + previous