# # Exercise

# The goal is to write a game program, call it randomgame.py,
# ask a user to guess a number for example between 1 and 10. 
# do that using the sys.argv by using 2 index arguements. 
# python3 [filename.py] [range1] [range2], python3 [0] [1] [2]
# get that information and try to randomly generate a number from that range
# from there the user can keep guessing until the user gets it right. 
# and at the and say when the user got it right that the terminal prints: You are a genius!, and
# if the user keeps getting it wrong the terminal will keep asking the user until the user gets it right
# and also use validation in the program as well to make sure that the user enters something that has been provided by the terminal with as an option. 

import random

import sys

class RangeError(Exception):
    pass


try:
    user_first_numr = int(sys.argv [1])
    user_second_numr = int(sys.argv [2])
except (ValueError, IndexError):
            print("Please enter a valid number")
            sys.exit()


r_num = random.randrange(user_first_numr, user_second_numr  + 1)

def user_guessing():
    while True:
        try:
            usr_g_num = int(input("Please guess and enter a number, the number between the numbers that you have entered:\n"))
            if user_first_numr <= usr_g_num <= user_second_numr:
                if usr_g_num == r_num:
                    print(f"You are a genius, the number was: {r_num}")
                    break
                else:
                    print("please try again")
            else:
                raise RangeError
        except ValueError:
            print("Please enter a valid number")
        except RangeError:
            print(f"{usr_g_num} is outside of specified range!")


def main():
    user_guessing()



if __name__=="__main__":
    main()

