string = input("Please type in a string: ")
substring = "aeo"
index = 0


while index < len(substring):
    if substring[index] in string:
        print(f"{substring[index]} found")
    else:
        print(f"{substring[index]} not found")
    
    index += 1
