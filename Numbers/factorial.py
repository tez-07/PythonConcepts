
def factorial(number):

    fac = 1
    for i in range(1, number + 1):
        fac *= i

    return fac

total = factorial(5)
print(total)
