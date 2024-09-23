start_range = int(input("Start of Range: "))
end_range = int(input("End of Range: "))

print("Special numbers in the range:")
for num in range(start_range, end_range + 1):
    original_num = num
    num_digits = 0
    sum_of_powers = 0

    temp = num
    while temp > 0:
        temp //= 10
        num_digits += 1

    temp = original_num
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_digits
        temp //= 10

    if sum_of_powers == original_num:
        print(original_num)