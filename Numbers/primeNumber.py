from itertools import count


class check():
    def primeNumber(self):
        num1 = int(input('Enter number:'))

        if num1 < 2:
            print('Not Prime')

        count = 0
        for i in range(1,num1+1):
            if num1 % i == 0:
                count += 1

        if count == 2:
            print('Prime')
        else:
            print('Not Prime')


c = check()
c.primeNumber()

