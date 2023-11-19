password = input("Password: ")
while True:
    password_confirmation = input("Repeat password: ")
    if password == password_confirmation:
        break
    else:
        print("They do not match!")
print("User account created!")