# inport library
import math


def area_of_figure(figure):
    # difine function
    
    result = 0

    if figure == "square":
        site = float(input())
        result = site ** 2

    elif figure == "rectangle":
        site_a = float(input())
        site_b = float(input())
        result = site_a * site_b

    elif figure == "circle":
        radius = float(input())
        result = math.pi * (radius ** 2)

    elif figure == "triangle":
        site = float(input())
        h = float(input())
        result = (site * h) / 2

    # return result
    return f"{result:.3f}"


# input
figure_arg = input()

# result
result = area_of_figure(figure_arg)

# print result
print(result)
