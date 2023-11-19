# Write your solution here
def squared(string, length):
    string_expanded = string * (length ** 2 // len(string) + 1)
    for index in range(0, length * length, length):
        row = string_expanded[index:index + length]
        print(row)