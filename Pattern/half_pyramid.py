'''
            *
            **
            ***
            ****
            *****
'''
from idlelib.outwin import file_line_progs


def halfPyramid():
    for i in range(5):
        for j in range(5):
            if i >= j:
                print('*', end='')
        print('')

halfPyramid()