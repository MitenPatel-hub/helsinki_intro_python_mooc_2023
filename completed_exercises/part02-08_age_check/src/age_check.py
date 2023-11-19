# Solution 1:

age = int(input("What is your age? "))

if age < 0:
    print("That must be a mistake")
elif age < 5:
    print("I suspect you can't write quite yet...")
else:
    print(f"Ok, you're {age} years old")

'''
# Solution 2: 

age = int(input("What is your age? "))

if age < 0:
    user_feedback = "That must be a mistake"
elif age < 5:
    user_feedback = "I suspect you can't write quite yet..."
else:
    user_feedback = f"Ok, you're {age} years old"

print(user_feedback)
'''