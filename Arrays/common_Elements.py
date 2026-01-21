

def commonElements_Arrays():
    arr1 = [23, 15, 37, 64, 51, 78]
    arr2 = [3, 15, 65, 24, 16, 80]

    arr3 = []
    for i in arr1:
        for j in arr2:
            if i == j:
                arr3.append(i)

    print(arr3)


commonElements_Arrays()