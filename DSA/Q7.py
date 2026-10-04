arr = [2, 5, 2, 8, 5, 2, 3, 5, 2]

max_count = 0
most_frequent = arr[0]

for n in arr:
    count = 0

    for x in arr:
        if n == x:
            count += 1

    if count > max_count:
        max_count = count
        most_frequent = n

print("Most Frequent Element:", most_frequent)
print("Frequency:", max_count)
