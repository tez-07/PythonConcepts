
def armstrongNumber(num):
    l =len(str(num))
    x = num
    sum = 0

    while x > 0:
        rem = x % 10
        prod = rem ** l
        sum += prod
        x = x // 10

    if sum == num:
        print(f'{num} is an armstrong number')
    else:
        print(f'{num} is not an armstrong number')

armstrongNumber(153)