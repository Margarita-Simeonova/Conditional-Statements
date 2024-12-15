def godzilla_vs_kong(budget, extras_count, clothing_price):

    decor = budget * 0.1

    # if statement
    if extras_count > 150:
        clothing_price *= 0.9

    total_price = decor + (clothing_price * extras_count)

    # if-else statement
    if total_price <= budget:
        return f"Action!\nWingard starts filming with {budget - total_price:.2f} leva left."
    else:
        return f"Not enough money!\nWingard needs {total_price - budget:.2f} leva more."


# input
money = float(input())
extras = int(input())
price_of_clothing = float(input())
# result
result = godzilla_vs_kong(money, extras, price_of_clothing)

print(result)
