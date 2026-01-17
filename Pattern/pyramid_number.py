'''
            1
          2  2
         3  3  3
        4 4  4  4
'''

def pyramidNumber():
    n = 5
    for i in range(1,n):
        for k in range(n-i):
            print(' ', end='')
        for j in range(i+1):
            print(i, end='')
        print('')

pyramidNumber()