

def mergeArrays():
    arr1 = [23, 5, 37, 64, 51, 78]
    arr2 = [3, 15, 65, 24, 16, 80]

    arr3 = [len(arr1) + len(arr2)]

    for i in arr1:
        arr3.append(i)

    for k in arr2:
        arr3.append(k)

    print(arr3)

mergeArrays()