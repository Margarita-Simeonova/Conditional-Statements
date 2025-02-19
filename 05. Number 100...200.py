def number_100_200(numb):
    # difine function
    
    if numb < 100:
        return "Less than 100"
    elif numb > 200:
        return "Greater than 200"

    else:
        return "Between 100 and 200"


# input
number = int(input())

# result
result = number_100_200(number)

# print result
print(result)
