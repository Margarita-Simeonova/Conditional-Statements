def toy_shop(vacation, puzzles, tolls, bears, minions, trucks):

	total_count = puzzles + tolls + bears + minions + trucks
	puzzles_price = puzzles * 2.6
	tolls_price = tolls * 3
	bears_price = bears * 4.1
	minions_price = minions * 8.2
	trucks_price = trucks * 2
	total_price = (puzzles_price + tolls_price + bears_price +
                   minions_price + trucks_price)

	if total_count >= 50:
		total_price *= 0.75

	total_price *= 0.9
	money_left = abs(total_price - vacation)

	if vacation <= total_price:

		return f"Yes! {money_left:.2f} lv left."
	return f"Not enough money! {money_left:.2f} lv needed."


vacation_price = float(input())
puzzles_count = int(input())
tolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())
print(toy_shop(vacation_price, puzzles_count, tolls_count, bears_count, minions_count, trucks_count))
