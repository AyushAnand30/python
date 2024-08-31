#print("Hellow world")
#n = int(input(" Enter your number: "))
from math import factorial
from operator import index

from setuptools.command.build_ext import if_dl


#def show(a):
    #if a == 0 :
       # return
    #else:
       # print(a)
       # return show(a - 1)
#show(5)
# def fect(n):
#     if n <=1:
#         return 1
#     else:
#
#         return n*fect(n-1)
# print(fect(5))

#sum of n natural number
# def cal_sum(n):
#     if(n <=1):
#         return n
#     else:
#         return n+cal_sum(n-1)
# print(cal_sum(100))


#print all the element of the list
def print_list(list, index =0):

    if index == len(list):
        return
    print(list[index])

    print(print_list(list,index+1))
num = [2, 3, 5, 7, 9, 11]

print(print_list(num))
