def shopping(budget, video_cards, processors, ram):

	video_cards_price = 250 * video_cards
	processors_price = (video_cards_price * 0.35) * processors
	ram_price = (video_cards_price * 0.10) * ram
	total_price = processors_price + ram_price + video_cards_price

	if video_cards > processors:
		total_price *= 0.85

	money_left = abs(total_price - budget)

	if total_price <= budget:

		return f"You have {money_left:.2f} leva left!"
	return f"Not enough money! You need {money_left:.2f} leva more!"


budget_for_shopping = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_count = int(input())
result = shopping(budget_for_shopping, video_cards_count, processors_count, ram_count)

print(result)
