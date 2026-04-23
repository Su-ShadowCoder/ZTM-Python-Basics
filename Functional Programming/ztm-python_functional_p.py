
#map # filter #zip # reduce

# from functools import reduce


# my_list= [1,2,3]


# def m_by2(item):
#     return item*2

# def only_odd(item):
#     return item % 2 != 0


# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item


# print(reduce(accumulator, my_list, 0))

# print(list(filter(only_odd, my_list)))

# print(my_list)

# print(list(zip(my_list, your_list)))

# from functools import reduce

# #1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']

# def cap_n(item):
#     return item.capitalize()

# print(list(map(cap_n, my_pets)))

# #2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5,4,3,2,1]

# print(list(zip(my_strings, my_numbers[::-1])))

# #3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]

# def g_s(item):
#     return item > 50

# print(list(filter(g_s, scores)))

# #4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

# def comb(l1, l2):
#     return l1 + l2 

# print(reduce(comb, scores, 0) + reduce(comb, my_numbers, 0))

# print(reduce(comb, (scores + my_numbers)))

# /////////////////////////////

# Lambda Expressions

# from functools import reduce

# lambda param: action(param)

# my_list= [1,2,3]


# # def multyply_by2(item):
# #     return item*2

# print(list(map(lambda item: item*2, my_list)))

# print(list(filter(lambda item: item % 2 != 0, my_list)))

# print(reduce(lambda acc, item: acc + item, my_list))

# /////////////////////////////

# Exercise: Lambda Expressions

#ssquare

# my_list = [5,4,3]

# print(list(map(lambda item: item**2, my_list)))

# # list sorting, second row in item sorted. 

# a = [(0,2), (4,3), (9,9), (10, -1)]



# # print(a[0][1].sort())

# print(sorted(a, key=lambda x: x[1]))

# a.sort()
# print(a)




# # /////////////////////////////

# # List Comprehensions

# # list, set, dictionary, datasets

# my_list = [element for element in "Hellow World"]

# my_list2 = [numb*2 for numb in range(0, 100)]

# my_list4 = [ numb for numb in range(0, 100) if numb % 2 == 0]

# print(my_list4)