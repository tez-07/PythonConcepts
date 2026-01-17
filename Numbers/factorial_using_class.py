
class Factorial():
    def __init__(self, num):
        self.num = num

    def calculation(self):
        fac = 1
        for i in range(1, self.num+1):
            fac *= i
        return fac

call = Factorial(5)
result =call.calculation()
print(result)