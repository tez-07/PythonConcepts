

def sort_Array():
    arr = [23, 5, 35, 64, 31, 78]

    for i in range(len(arr)):
        for k in range(i+1, len(arr)):
            if arr[i] > arr[k]:
                arr[i], arr[k] = arr[k], arr[i]


    print(arr)

sort_Array()



def sort_using_Built_In_Function():
    arr = [23, 5, 35, 64, 31, 78]
    arr.sort()
    print(arr)

sort_using_Built_In_Function()