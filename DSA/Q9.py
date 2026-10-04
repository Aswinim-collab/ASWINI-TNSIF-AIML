arr1 = [1, 2, 2, 3, 4]
arr2 = [4, 2, 1, 2, 3]

if len(arr1) != len(arr2):
    print("Arrays are Not Equal")
else:
    count1 = {}
    count2 = {}

    for n in arr1:
        count1[n] = count1.get(n, 0) + 1

    for n in arr2:
        count2[n] = count2.get(n, 0) + 1

    if count1 == count2:
        print("Arrays are Equal")
    else:
        print("Arrays are Not Equal")
