"""
# ----------------------
# Created : 11-11-2021 23:57
# Licencing : (C) 2021 Dalimol Abraham, LYIT
#             Available under GNU public licence
# Description: 
# Author : Dalimol Abraham
# ----------------------
"""


# '''Static Type Checking example '''

def factorial(num):
    '''Factorial is where you have factors of a number
       3! == 3x2x1 == 6
       2! == 2x1 == 2
       1! == 1x1 == 1
    '''
    if num < 0:
        return None
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1);


if __name__ == "__main__":
    print(factorial(2))

'''Static typec chwck'''
