import math


def radians_to_degrees(rad):
    degrees = rad * 180 / math.pi

    return degrees


radians = float(input())
print(radians_to_degrees(radians))

