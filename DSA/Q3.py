arr = [10, -5, 20, -8, 15, -2]

positive_sum = 0
negative_sum = 0

for n in arr:
    if n > 0:
        positive_sum += n
    elif n < 0:
        negative_sum += n

print("Positive Sum:", positive_sum)
print("Negative Sum:", negative_sum)
