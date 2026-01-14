'''
            *******
            *     *
            *     *
            *     *
            *******

Take out the indexes where star can be formed.
'''


def hollow_square():

    n = 5
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or i==n-1 or j==n-1:        # i and j should either be 0 or n-1(4)
                print('*', end='')
            else:
                print(' ', end='')
        print()

hollow_square()


