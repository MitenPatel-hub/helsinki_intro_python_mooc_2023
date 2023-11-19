lunches_per_week = int(input("How many times a week do you eat at the student cafeteria? "))
price_per_lunch = float(input("The price of a typical student lunch? "))
grocery_cost_per_week = float(input("How much money do you spend on groceries in a week? "))

weekly_food_cost = lunches_per_week * price_per_lunch + grocery_cost_per_week
daily_food_cost = weekly_food_cost / 7

print("Average food expenditures:")
print(f"Daily: {daily_food_cost} euros")
print(f"Weekly: {weekly_food_cost} euros")