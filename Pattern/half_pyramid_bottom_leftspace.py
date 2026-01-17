'''
            *****
             ****
              ***
               **
                *
'''



def half_pyramid180():
    n = 5
    for i in range(n):
        for spaces in range(i):
            print(' ', end='')
        for stars in range(n-i):
            print('*', end='')
        print('')

half_pyramid180()
