from operator import length_hint
from os import remove

from Numbers.factorial import total


def armstrongNumber(num):
    l =len(str(num))

    sum = 0
    total = 0
    while num > 0:
        rem = num % 10
        sum += rem
        for k in range(l):
            total = sum * k
        num = num // 10

    return total, sum


s = armstrongNumber(153)
print(s)