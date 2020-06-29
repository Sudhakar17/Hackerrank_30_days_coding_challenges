# Question Link:
# https://www.hackerrank.com/challenges/30-operators/problem

"""Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
    and tax percent (the percentage of the meal price being added as tax) for a meal,
    find and print the meal's total cost."""


import sys
def calculate_meal_cost():
    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)

    total_cost = round(meal_cost + tip + tax)
    print("The total meal cost is {} dollars.".format(total_cost))


if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    calculate_meal_cost()