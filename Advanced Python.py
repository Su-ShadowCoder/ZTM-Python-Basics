

# @decorator
# def hellow():
#     print("hellow")

# # a higher order function  is a funciton that accepts another function. 


# def greet(func):
#     func()

# def greet2():
#     def func():
#         return 5
#     return func

# map etc are higher order function. 


# a decorator is a function that has a function and enhanches or chnages it that function

# def my_dec(func): #when you see this you know it is a higher order funciton if the param is another function name. 
#     def wrap_func():
#         print("***********")
#         func()
#         print("***********")
#     return wrap_func

# # @my_dec
# def hello():
#     print("hello")
# # @my_dec
# def bye():
#     print("smell ye later")

# bye()

# # what actually is happening is 

# hello2 = my_dec(hello)

# hello2()


# Decorator Pattern

# def my_decorator(func):
#     def wrap_funct(*args, **kwargs):
#         print("**********")
#         func(*args, **kwargs)
#         print("**********")
#     return wrap_funct

# @my_decorator
# def hello(param, emoji=":)"):
#     print(param, emoji)

# hello("hii")


# Decorator
# from time import time


# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, **kwargs)
#         t2 = time()
#         print(f"took {t2-t1} s")
#         return result
#     return wrapper

# @performance
# def long_time():
#     for i in range(100000000):
#         i*5

# long_time()


# DECORATOR (Function Enhancer) : A reusable wrapper used to add logic (like 
#     security or logging) to multiple functions without repeating code.
#     - Focus: Behavior/Action ("What it does").
#     - Benefit: Fix it in one place, it updates everywhere.

# CLASS ATTRIBUTES (Object Stats) : Shared properties that belong to a class 
#     structure and all objects created from it.
#     - Focus: Data/Identity ("What it is").
#     - Benefit: Ensures all objects of a certain type stay consistent.


# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# user1 = {
#     'name': 'Sorna',
#     'valid': True #changing this will either run or not run the message_friends function.
# }

# def authenticated(fn):
#     def wrapper(*args, **kwargs):
#         user = args[0]
#         if user.get("valid"):
#             fn(*args, **kwargs)
#         else:
#             print("invalid user")
#     return wrapper
        



# @authenticated
# def message_friends(user):
#     print('message has been sent')

# message_friends(user1)


# /////////////////////////////////

# ================================================================================
#                  PYTHON PREVIEW: SECURITY & PERSISTENCE
# ================================================================================

# 1. ERROR HANDLING (The Shield)
#    - Logic: 'try' to run code, 'except' an error happens, 'finally' clean up.
#    - Security: Prevents the system from crashing and leaking "Stack Traces" 
#      (system secrets) to an attacker.

# 2. FILE I/O (Storage Disk Interaction)
#    - Logic: Open a Path, Read/Write data, and CLOSE the connection.
#    - Persistence: This is how a System saves its "State" so data isn't lost 
#      when the Process ends or the Hardware reboots.
# ================================================================================

# Errors in Python


# Error HANDLING 

# while True:
#     try:
#         age = int(input("what is your age\n"))
#         10/age
#     except ValueError:
#         print("Please enter a number!")
#     except ValueError:
#         print("!!!!!!")
#     except ZeroDivisionError:
#         print("Please enter age higher thatn 0")

#     else:
#         print("thank you")
#         break

# def sum(num1, num2):
#         try:
#             return num1 / num2
#         except (TypeError, ZeroDivisionError) as err:
#             print(err)




# print(sum(9, '0'))


# while True:
#     try:
#         age = int(input("what is your age\n"))
#         10/age
#         raise Exception("hey cut it out")
#     except ValueError:
#         print("Please enter a number!")
#     except ValueError:
#         print("!!!!!!")
#     except ZeroDivisionError:
#         print("Please enter age higher thatn 0")
#     else:
#         print("thank you")
#         break
#     finally:
#         print("ok, i am finally done")



# Advanced Python: Generators



# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result

# my_list = make_list(100)
# print(my_list)

# generator
# def generator_function(num):
#     for i in range(num):
#         yield i* 2

# g = generator_function(100)
# next(g)
# next(g)
# print(next(g))



# //////////////////////

# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             print(next(iterator))
#         except StopIteration:
#             break

# special_for([1,2,3])



# //////////////////////////////////////
# Under The Hood Of Generators

# equivalant of what range() kinda is 
# class MyGen():
#     current = 0
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if MyGen.current < self.last:
#             num = MyGen.current
#             MyGen.current += 1
#             return num
#         raise StopIteration

# gen = MyGen(0, 100)

# for i in gen:
#     print(i)

# /////////////////////////////////////

# Exercise Fibonacci Numbers

# with generator 
# def fib(number):
#     a = 0
#     b = 1
#     for num in range(0, number+1):
#         yield a
#         temp = a 
#         a = b 
#         b = temp + b 

# for x in fib(20):
#     print(x)

# /////////////////

# with memory 
# def fib2(number):
#     a = 0
#     b = 1
#     result = []
#     for num in range(0, number+1):
#         result.append(a)
#         temp = a 
#         a = b 
#         b = temp + b
#     return result

# print(fib2(40))

