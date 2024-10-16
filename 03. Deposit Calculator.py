def deposit_calculator(deposit_sum, period_in_mounts, interest_rate):
    total_sum = deposit_sum + period_in_mounts * ((deposit_sum * interest_rate / 100) / 12)

    return total_sum


deposit = float(input())
mounts = int(input())
percent = float(input())
print(deposit_calculator(deposit, mounts, percent))
