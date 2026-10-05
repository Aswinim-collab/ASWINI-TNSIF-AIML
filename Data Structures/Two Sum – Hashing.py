def two_sum(arr, target):
    seen = {}

    for i in range(len(arr)):
        complement = target - arr[i]

        if complement in seen:
            return [seen[complement], i]

        seen[arr[i]] = i

    return []


arr = [2, 7, 11, 15]
target = 9

print(two_sum(arr, target))
