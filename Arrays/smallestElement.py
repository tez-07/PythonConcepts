

def smallest_element():
    arr = [23, 5, 35, 64, 31, 78]

    smallest = arr[0]
    for i in arr[1:]:           #slicing: arr[start : end]
        if i < smallest:
            smallest = i

    return  smallest


print(smallest_element())