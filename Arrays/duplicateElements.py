

def duplicate_Elements_Array():
    arr = [23, 55, 35, 23, 64, 31, 78]

    dup_arr = []

    for i in range(len(arr)):                   #starting from 0th index
        for j in range(i+1, len(arr)):          #starting from 1st index
            if arr[i] == arr[j]:
                dup_arr.append(arr[i])

    print(dup_arr)


duplicate_Elements_Array()