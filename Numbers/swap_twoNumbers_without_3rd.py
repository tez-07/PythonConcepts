
def swapNumbersWithoutUsingThirdNumber():
    number1 = int(input('Enter your first number:'))
    number2 = int(input('Enter your second number:'))


    number1, number2 = number2, number1
    print(f'After Swapping Numbers: number1: {number1} and number2: {number2}')


swapNumbersWithoutUsingThirdNumber()
