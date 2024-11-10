import math


def area_of_figure(figure):
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

    return f"{result:.3f}"


figure_arg = input()
result = area_of_figure(figure_arg)

print(result)
