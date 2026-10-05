def longest_consecutive(arr):
    numbers = set(arr)
    maximum = 0

    for num in numbers:
        if num - 1 not in numbers:
            current = num
            length = 1

            while current + 1 in numbers:
                current += 1
                length += 1

            maximum = max(maximum, length)

    return maximum


arr = [100, 4, 200, 1, 3, 2]

print(longest_consecutive(arr))
