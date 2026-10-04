arr = [1, 2, 3, 4, 5]
k = 2

k = k % len(arr)

result = arr[-k:] + arr[:-k]

print(result)
