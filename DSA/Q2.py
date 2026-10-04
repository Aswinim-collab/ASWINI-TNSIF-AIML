arr = [10, 5, 0, 7, 8, 0, 13, 4]

even = 0
odd = 0
zero = 0

for n in arr:
    if n == 0:
        zero += 1
    elif n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)
print("Zero:", zero)
