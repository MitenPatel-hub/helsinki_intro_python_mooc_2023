# My Solution
word = input("Please type in a word: ")
char = input("Please type in a character: ")

if char in word:
    first_index = word.find(char)
    slice = word[first_index]
    if first_index + 2 <= len(word) - 1:
        last_index = first_index + 2
        while first_index < last_index:
            previous = slice
            first_index += 1
            slice = previous + word[first_index]

        print(slice)
'''
# Model Solution
word = input("Please type in a word: ")
character = input("Please type in a character: ")
 
index = word.find(character)
if index != -1 and len(word) >= index + 3:
    print(word[index:index + 3])
'''