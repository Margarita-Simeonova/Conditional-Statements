def speed_info(speed):
	# difine function
	
	if speed <= 10:
		return "slow"
	elif 10 < speed <= 50:
		return "average"
	elif 50 < speed <= 150:
		return "fast"
	elif 150 < speed <= 1000:
		return "ultra fast"
	elif speed > 1000:
		return "extremely fast"


# input
speed = float(input())

# result
result = speed_info(speed)

# print result
print(result)
