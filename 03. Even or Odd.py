def even_or_odd(numb):

    if numb % 2 == 0:
        return "even"
    else:
        return "odd"


number = int(input())
print(even_or_odd(number))
