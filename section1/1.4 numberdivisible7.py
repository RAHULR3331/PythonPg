def find_numbers():
    count = 0
    total_sum = 0

    for num in range(101, 200):
        if num % 7 == 0:
            count += 1
            total_sum += num

    return count, total_sum


count, total_sum = find_numbers()

print(f"Number of integers divisible by 7 between 101 and 200: {count}")
print(f"Sum of integers divisible by 7 between 101 and 200: {total_sum}")
