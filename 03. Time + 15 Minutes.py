def time_15_min(hours, minutes):

    time_in_minutes = (hours * 60)
    time = time_in_minutes + minutes + 15

    total_time_in_hours = time // 60
    total_time_in_minutes = time % 60

    if total_time_in_hours >= 24:
        total_time_in_hours = 0

    if total_time_in_minutes >= 60:
        total_time_in_hours += 1
        total_time_in_minutes = 0

    if total_time_in_minutes < 10:
        return f"{total_time_in_hours}:0{total_time_in_minutes}"
    else:
        return f"{total_time_in_hours}:{total_time_in_minutes}"


input_hour = int(input())
input_minutes = int(input())
print(time_15_min(input_hour, input_minutes))