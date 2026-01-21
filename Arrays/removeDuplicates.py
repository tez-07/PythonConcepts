

def removeDuplicates():
    arr = [23, 5, 23, 35, 64, 31, 78]
    new_arr = []

    for i in arr:
        if i not in new_arr:
            new_arr.append(i)

    print(new_arr)

removeDuplicates()