

def second_largest():
    arr = [23,5,35,64,31,78]

    largest = 0
    secondlargest = 0

    if arr[0] > arr[1]:
        largest = arr[0]
        secondlargest = arr[1]
    else:
        largest = arr[1]
        secondlargest = arr[0]


    for i in range(2, len(arr)):
        if arr[i] > largest:
            secondlargest = largest
            largest = arr[i]
        elif arr[i] > secondlargest:
            secondlargest = arr[i]

    print(f'largest: {largest}, secondlargest:{secondlargest}')

second_largest()



