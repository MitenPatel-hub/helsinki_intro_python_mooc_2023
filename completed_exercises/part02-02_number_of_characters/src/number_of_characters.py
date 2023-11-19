'''
# Solution 1
word = input("Please type in a word: ")

if len(word) > 1:
    print(f"There are {len(word)} letters in the word {word}")

print("Thank you!")
'''

# Solution 2

word = input("Please type in a word: ")
word_length = len(word)

if word_length > 1:
    print(f"There are {word_length} letters in the word {word}")

print("Thank you!")