

def largest_Number():

    size = int(input(f'Enter the size:'))
    arr = []

    for i in range(size):
        arr.append(int(input(f'Enter element {i + 1}: ')))

    print("array: ", arr)

    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i

    return largest


c = largest_Number()
print(c)