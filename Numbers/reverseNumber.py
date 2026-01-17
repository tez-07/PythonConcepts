from os import remove


def reverseNumber(num):

    reverse = 0
    while num > 0:
        rem = num % 10
        reverse = reverse * 10 + rem
        num = num // 10
    return  reverse

print(reverseNumber(123))
