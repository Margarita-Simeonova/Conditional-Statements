def sum_seconds(first_time, second_time, third_time):

    total_sum = first_time + second_time + third_time

    time_in_minutes = total_sum // 60
    time_in_seconds = total_sum % 60

    if time_in_seconds < 10:
        return f"{time_in_minutes}:0{time_in_seconds}"
    else:
        return f"{time_in_minutes}:{time_in_seconds}"


# take input
time_1 = int(input())
time_2 = int(input())
time_3 = int(input())
result = sum_seconds(time_1, time_2, time_3)

print(result)
