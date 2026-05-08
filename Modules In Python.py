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

# //////////////////////////////////////////////


# //////////////////////////////////////////////

# Lesson: Useful Modules 2


# import datetime


# print(datetime.time())

# print(datetime.time(1,15,10))

# print(datetime.date.today())

# today_week_day = datetime.date.today()

# print(datetime.date.weekday(today_week_day))


# from array import array

# arr = array('i', [1,2,3])

# print(arr[0])

# //////////////////////////////////////////////


# //////////////////////////////////////////////

# Lesson: How To Debug Code


# mistakes in code of a program that causes the the program not work, are called bugs. as you keep trying to solve those mistakes and improve the code you are doing the act of debugging. 

# Programs are full of errors or what we call bugss or for an even more convoluted term: Exceptions. 

# The act of finding and removing these bugs/errors from the code is called debugging. 

# Tools and good practices to debug:
# -linting = is an extension or build in ide tool that highlights and supports you while you are coding. linting allows you to find errors before you even run the code. 
# - using IDE's or Editor's = which has build-in tools that also supports you in writing good code and supports you to write if you set it right in accordance with the PEP8 conventions.
# - Read errors = how to read error message properly and translate that what problem the python interpreter is running into. by doing so then understanding what the bug in the code is or the mistake. 
# - reading python documentations about different kind of errors and recognizing them so you know what error you get, in turn allows you to then translate the error messages so you know where and what the bugs are.
# - pdb = is a build in module in python which is part of the standard python library. use .settrace() from pdb. a method to translate an error very efficiently
# - using print also is a good method to highligh  if something is working or not in the output. 

# //////////////////////////////////////////////


# //////////////////////////////////////////////

# Lesson: Working With Files In Python


# FILE I/O = I/O stands for input output. 

# input image/pdf/what everyou want to work with
# out compressed image, etc

# with the open key word you can choose a file to work with



# my_file = open("file1.txt")

# print(my_file)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readlines())

# my_file.close()



# This read method is an open cursor, 
# once you execute it it can only do it once before you do it the next time
# with the seek method you can loophole that do read/print the file content multiple times.

# After openning the file you have to manually close the file. so you can use this file somewhere 
# else in the program.

# //////////////////////////////////////////////


# //////////////////////////////////////////////
# Lesson: Read, Write, Append


# with open('file1.txt') as my_file:
# 	print(my_file.readlines())

# with open("file1.txt", mode='r+') as my_file:
# 	text = my_file.write(':D')
# 	print(text) 

# with mode r it only reads the file. without the mode it
# automatically asummes you are reading.

# if you want to write a file, you use the letter w. as mode='w'
#  mode=r+ is for read and write.

# when rewriting  the same text file you have to carefale that it would try to overwrite
# and by proxy the new text will overwrite the old text, but in accordance with its length, 
# which means that if there is a longer old text then the new text will only overwrite the amount
# of characters it has and leaves the old text for the rest of its characters as it is.

# In order to avoid doing that you use the append mode as here under in the example:
# with open("file1.txt", mode='a') as my_file:
# 	text = my_file.write(':D')
# 	print(text) 

# r to read
# w to write - this will asume its a new file and we write a new
# a to append add things properly without overwriting when in r+
# r+ to read and write

# with open("file1.txt", mode='w') as my_file:
# 	text = my_file.write(':D')
# 	print(text) 

# be carefull that you use the right mode based on what you need. 

# with open('app/sad.txt', mode='r') as my_file:
# 	print(my_file.read())


# w = write also creates a new file if it doesnt exist already or overwrites the existing 
# one completely


# This method of accessing the files is called absolute path 

# with open('/home/abdullah/Desktop/app/sad.txt', mode='r') as my_file:
# 	print(my_file.read())

# sometimes you might see ./ this means from the current folder

# with open('./app/sad.txt', mode='r') as my_file:
# 	print(my_file.read())


# The pathlib module allows your code to work with both linux and windows filesystem paths
# Object-oriented filesystem paths


# lesson: File IO Errors 

# try:
# 	with open('sad.txt', mode='x') as my_file:
# 		print(my_file.read())
# except FileNotFoundError as err:
# 	print("file does not exist!")
# 	raise err
# except IOError as err:
# 	print("IO Error!")
# 	raise err


# //////////////////////////////////////////////


# //////////////////////////////////////////////
# Lesson: Exercise: Translator


# //////////////////////////////////////////////


# //////////////////////////////////////////////
# Lesson: