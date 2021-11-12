"""
# ----------------------
# Created : 11-11-2021 20:32
# Licencing : (C) 2021 Dalimol Abraham, LYIT
#             Available under GNU public licence
# Description: 
# Author : Dalimol Abraham
# ----------------------
"""

print("Enter a number between 1 to 15")

game_start = int(input("Do you want to start the game (1/0)? "))

while game_start == 1:
    enter_value = int(input('Enter your number: '))
    guess_value = 10
    if enter_value == 10:  # guess the correct value
        print('Success')
        break
    elif enter_value > 10:
        print('Your entered value is exceeded the number')
    elif enter_value < 10:
        print('Your entered value is under imagination')
    game_start = int(input("Do you want to continue the game (1/0)? "))
else:
    print('Exit')
