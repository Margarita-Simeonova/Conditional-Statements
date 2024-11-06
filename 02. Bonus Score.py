def bonus_score(number):

    result = 0

    if number <= 100:
        result += 5
    elif number > 1000:
        result += number * 0.1
    elif number > 100:
        result += number * 0.2

    if number % 2 == 0:
        result += 1
    elif number % 10 == 5:
        result += 2

    return f"{result}\n{result + number}"


numb = int(input())
result = bonus_score(numb)

print(result)
