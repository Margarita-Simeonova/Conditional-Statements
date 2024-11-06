def greater_number(numb_1, numb_2):

    if numb_1 > numb_2:
        return numb_1

    else:
        return numb_2


first_number = int(input())
second_number = int(input())
result = greater_number(first_number, second_number)
print(result)
