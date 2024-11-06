def even_or_odd(numb):

    if numb % 2 == 0:
        return "even"
    else:
        return "odd"


number = int(input())
result = even_or_odd(number)
print(result)
