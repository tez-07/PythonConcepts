#1, 2, 3, 5, 8, 13, 21, 34

def fibonacci(num):

    sum = 0
    pnum = 0
    nnum = 1
    for i in range(1, num):
        sum = pnum + nnum
        print(sum)
        pnum = nnum
        nnum = sum

c = fibonacci(5)
print(c)