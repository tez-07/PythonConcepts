'''
        ****
        ****
        ****
        ****
'''


# 1st Way:
def square_pattern():
    for i in range(0,4):
        for k in range(0,4):
            print('*', end='')          # Prints * + NOTHING → stays on same line
        print()

square_pattern()


# 2nd Way:
def square():
    for i in range(4):
        print('****')

square()