'''
        *
       **
      ***
     ****
    *****
'''

def halfPyramid_leftspace():
    n = 4  # Max width
    for i in range(n + 1):
        for j in range(n-i):        #4 spaces: " " for i= 0
            print(' ', end='')
        for k in range(i+1):        #1 star: "*" for i= 0
            print('*', end='')
        print('')

halfPyramid_leftspace()