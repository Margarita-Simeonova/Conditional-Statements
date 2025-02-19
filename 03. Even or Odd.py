def even_or_odd(numb):

    if numb % 2 == 0:
        return "even"
    else:
        return "odd"


# input
number = int(input())

# result
result = even_or_odd(number)
print(result)
