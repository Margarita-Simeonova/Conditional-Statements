import math


def world_swimming_record(best_time, distance, time_per_meter):

    swimming_time = distance * time_per_meter
    delay = (math.floor(distance / 15)) * 12.5
    total_time = swimming_time + delay

    difference = abs(total_time - best_time)

    if total_time < best_time:
        return f"Yes, he succeeded! The new world record is {total_time:.2f} seconds."
    else:
        return f"No, he failed! He was {difference:.2f} seconds slower."


record = float(input())
metres = float(input())
time = float(input())
result = world_swimming_record(record, metres, time)
print(result)
