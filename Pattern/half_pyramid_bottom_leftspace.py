'''
            *****
             ****
              ***
               **
                *
'''
from idlelib.outwin import file_line_progs


def half_pyramid180():
    for i in range(5):
        for k in range(5):
            if i >= k:
                print('*',end='')
        print('')

half_pyramid180()
