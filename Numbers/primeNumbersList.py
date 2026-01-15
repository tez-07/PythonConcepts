

class checkPrime():
    def primeNumbers(self):
        n1 = int(input('Enter number from:'))
        n2 = int(input('Enter number till:'))

        allPrime = []
        count = 0
        for i in range(n1, n2+1):
            if i<2:
                continue

            isPrime = True
            for k in range(2,i):
                if i % k == 0:
                    isPrime = False
                    break

            if isPrime:
                allPrime.append(i)
        print(allPrime)

c = checkPrime()
c.primeNumbers()