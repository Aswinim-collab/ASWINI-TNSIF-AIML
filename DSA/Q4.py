arr = [10, 20, 10, 30, 20, 40, 30]

result = []

for n in arr:
    if n not in result:
        result.append(n)

print(result)
