# a package is a folder


# import packagename.modulename

# Python is extrememly usefull because of externel module packages, in which you can borrow and extend the program code functionality. These are called python build in modules. 


# there is extensive module library in existence which you even can find on the python homepage, there isa extensive list where you can find all kinds of modules. This is called the standard python library. this library comes with the python that you have installed. 

# so when you code and build something and you need functions that helps you with what you are building, you can the search for its corresponging module on the internet, like python module "example" . most likely there would be, and other wise you might have to search more on different places, and if there realy is nothing you build your own file with functions and finaly import it as a module that you yourself have crafted. 


# import random

# print(dir(random.))

# print(random.randint(1, 19))

# print(random.choice([1,2,4,5]))

# my_list = list(range(0, 10))

# random.shuffle(my_list)

# print(my_list)

# when importing something from the standard library its better to from module import what is necessary  so people know what it is. 

# import sys


# sys.argv

# Exercise

# The goal is to write a game program, call it randomgame.py,
# ask a user to guess a number for example between 1 and 10. 
# do that using the sys.argv by using 2 index arguements. 
# python3 [filename.py] [range1] [range2], python3 [0] [1] [2]
# get that information and try to randomly generate a number from that range
# from there the user can keep guessing until the user gets it right. 
# and at the and say when the user got it right that the terminal prints: You are a genius!, and
# if the user keeps getting it wrong the terminal will keep asking the user until the user gets it right
# and also use validation in the program as well to make sure that the user enters something that has been provided by the terminal with as an option. 


# import random

# import sys

# class RangeError(Exception):
#     pass


# try:
#     user_first_numr = int(sys.argv [1])
#     user_second_numr = int(sys.argv [2])
# except (ValueError, IndexError):
#             print("Please enter a valid number")
#             sys.exit()


# r_num = random.randrange(user_first_numr, user_second_numr  + 1)

# def user_guessing():
#     while True:
#         try:
#             usr_g_num = int(input("Please guess and enter a number, the number between the numbers that you have entered:\n"))
#             if user_first_numr <= usr_g_num <= user_second_numr:
#                 if usr_g_num == r_num:
#                     print(f"You are a genius, the number was: {r_num}")
#                     break
#                 else:
#                     print("please try again")
#             else:
#                 raise RangeError
#         except ValueError:
#             print("Please enter a valid number")
#         except RangeError:
#             print(f"{usr_g_num} is outside of specified range!")


# def main():
#     user_guessing()



# if __name__=="__main__":
#     main()

# //////////////////////////////////////////////


# //////////////////////////////////////////////

# Lesson: Python Package Index

# The reason why python is becoming mainstraim and is being used a lot is because there are a lot of people out there that are already making their modules for different kind of concept, which means that you dont have to reinvent the wheel. so you have the standard library and also the whole internet worth of modules made by all kinds of people for all kinds of things, and if not then you make your own, and you share that with the internet, which in turn make others use your modules by downloading and importing it. 

# with this we are able to use eachothers code. we are able to do that by using the pip install command. basically standing on the shoulders of giant. 

# You can access this collective internet module library/repository is called:
# www.pypi.org
# python package index

# A good practice is to first check that something exist in the standdard python library that has to do with the program that you are going to code. and if you cant find it there you go to pypi.org 

# sometimes you want to use extra features that the standard python modules not have then you can also check the pypi modules and import that as you might find something you want to use that is not in the python library module. 

# //////////////////////////////////////////////


# //////////////////////////////////////////////

# Lesson: pip install

# either install it via editor or do it manually trough the terminal. but nowadays you should make a virtual envirement to add pypi modules manually. check the IT-Manual for procedure. 