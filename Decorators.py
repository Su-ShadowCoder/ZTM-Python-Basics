

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


