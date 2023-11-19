'''
# Does not work, but should work
sentence = input("Please type in a sentence: ")
i = 0
while i < len(sentence):
    print(sentence[i])
    while sentence[i] != " ":
        i += 1
        if i == len(sentence) - 1:
            continue
    i += 1  

# Works
sentence = input("Please type in a sentence: ")
i = 0
while i < len(sentence):
    print(sentence[i])
    while sentence[i] != " ":
        if i < len(sentence) - 1:
            i += 1
    i += 1  

# Works
sentence = input("Please type in a sentence: ")
i = 0
while i < len(sentence) - 1:
    print(sentence[i])
    while sentence[i] != " " and i < len(sentence) - 1:
        i += 1
    i += 1

# Works
sentence = input("Please type in a sentence: ")
i = 0
while i < len(sentence):
    print(sentence[i])
    while sentence[i] != " ":
        if i < len(sentence) - 1:
            i += 1
    i += 1  
    '''
sentence = input("Please type in a sentence: ")
i = 0
while i < len(sentence) - 1:
    print(sentence[i])
    while sentence[i] != " " and i < len(sentence) - 1:
        i += 1
    i += 1