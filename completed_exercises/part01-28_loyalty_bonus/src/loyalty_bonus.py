points = int(input("How many points are on your card? "))
ten_percent_bonus = points * 1.1
fifteen_percent_bonus = points * 1.15

if points < 100:
    print("Your bonus is 10 %")
    print("You now have", ten_percent_bonus, "points")

if points >= 100:
    print("Your bonus is 15 %")
    print("You now have", fifteen_percent_bonus, "points")