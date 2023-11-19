letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")
middle_letter = ""

if letter1 > letter2:
  if letter3 > letter1:
    middle_letter = letter1
  elif letter2 > letter3: 
    middle_letter = letter2
  else: 
    middle_letter = letter3

if letter2 > letter1:
  if letter1 > letter3:
    middle_letter = letter1
  elif letter3 > letter2:
    middle_letter = letter2
  else:
    middle_letter = letter3

print(f"The letter in the middle is {middle_letter}")