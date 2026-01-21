


def reverseArray():
    arr = [23, 5, 35, 64, 31, 78]

    '''
        len(arr) -1 : starting point
        stop → -1 (not included) || stop is always excluded, no matter the direction.
        step → -1 (go backwards)
    '''
    for i in range(len(arr) -1, -1, -1):
        print(arr[i])



reverseArray()