word = ""
new_word = ""
words = ""

while True:
    word = input("Please type in a word: ")
    if word == "end":
        break
    elif word == new_word:
        break
    
    new_word = input("Please type in a word: ")
    if new_word == "end":
        words += word
        break
    elif new_word == word:
        words += word
        break
    else:
        words += word + " " + new_word
    
    words += " "

print(words)