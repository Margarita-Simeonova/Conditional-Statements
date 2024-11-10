import math


def lunch_break(name, series_time, break_time):

	lunch_time = break_time / 8
	relax = break_time / 4
	time_left = break_time - lunch_time - relax

	time = abs(time_left - series_time)

	if series_time <= time_left:

		return f"You have enough time to watch {name} and" \
		       f" left with {math.ceil(time)} minutes free time."
	return f"You don't have enough time to watch " \
	       f"{name}, you need {math.ceil(time)} more minutes."


movie_name = input()
movie_time = int(input())
break_time = int(input())
result = lunch_break(movie_name, movie_time, break_time)

print(result)
