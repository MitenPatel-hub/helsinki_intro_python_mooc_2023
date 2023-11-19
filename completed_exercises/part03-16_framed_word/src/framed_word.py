'''
# Solution 1
word = input("Word: ")
asterisk = "*"
row_asterisks = asterisk * 30
spaces = " " * int((30 - len(word)) / 2 - 1)
spaces_odd_right = " " * int(((30 - len(word)) / 2 - 1) + 1)
even_word_row = f"{asterisk}{spaces}{word}{spaces}{asterisk}"
odd_word_row = f"{asterisk}{spaces}{word}{spaces_odd_right}{asterisk}"

if len(word) % 2 == 0:
    print(row_asterisks)
    print(even_word_row)
    print(row_asterisks)
else:
    print(row_asterisks)
    print(odd_word_row)
    print(row_asterisks)

# Solution 2
word = input("Word: ")
row_asterisks = "*" * 30
even_word_row = f"*{' ' * int((30 - len(word)) / 2 - 1)}{word}{' ' * int((30 - len(word)) / 2 - 1)}*"
odd_word_row = f"*{' ' * int((30 - len(word)) / 2 - 1)}{word}{' ' * int(((30 - len(word)) / 2 - 1) + 1)}*"

if len(word) % 2 == 0:
    print(row_asterisks)
    print(even_word_row)
    print(row_asterisks)
else:
    print(row_asterisks)
    print(odd_word_row)
    print(row_asterisks)

# Solution 3
word = input("Word: ")
row_asterisks = "*" * 30
even_word_row = f"*{' ' * int((len(row_asterisks) - len(word) - 2) / 2)}{word}{' ' * int((len(row_asterisks) - len(word) - 2) / 2)}*"
odd_word_row = f"*{' ' * int((len(row_asterisks) - len(word) - 2) / 2)}{word}{' ' * int((len(row_asterisks) - len(word)) / 2)}*"

if len(word) % 2 == 0:
    print(row_asterisks)
    print(even_word_row)
    print(row_asterisks)
else:
    print(row_asterisks)
    print(odd_word_row)
    print(row_asterisks)
'''
# Solution 4
word = input("Word: ")
row_asterisks = "*" * 30

if len(word) % 2 == 0:
    print(row_asterisks)
    print(f"*{' ' * int((len(row_asterisks) - len(word) - 2) / 2)}{word}{' ' * int((len(row_asterisks) - len(word) - 2) / 2)}*")
    print(row_asterisks)
else:
    print(row_asterisks)
    print(f"*{' ' * int((len(row_asterisks) - len(word) - 2) / 2)}{word}{' ' * int((len(row_asterisks) - len(word)) / 2)}*")
    print(row_asterisks)