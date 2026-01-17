from os import remove


def sumofDigits(number):

    sum = 0
    while number > 0:
        rem =  number % 10
        sum += rem
        number = number // 10
    return sum

total = sumofDigits(121)
print(total)