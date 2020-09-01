# -*- coding: utf-8 -*-
"""
Created on Wed May 13 01:34:27 2020

@author: sakshi
"""

# object or data types in python

# 1) tuple
# 2) list
# 3) dictionary
# 4) sets


# for runnning code in jupyter 
# shift enter
# crtl enter
# alt enter

# if jupyter get hanged then go to kernal and then restart it

# tuple ( its a 1 dimensional representation of elements 
# which can be of mixed types and it is immutable)

tup1 = (2,4,5,6,7,8,'pune')
type(tup1)

tup1
tup1[2]
tup1[2] = 500# once created it can not be changed

tup2 = (2,4,5,6,7,8,9,9,9,9,'pune')
tup2.count(9)# kitne bar occur kr raha hai number
# count give answer of count of the given number in the bracket

tup2.index(4)

# kha pr occur kr raha hai number
# it is given the position of that number which is given in bracket
tup2.index(8)

t1 = 10,2,100,200 # we can write tuple in this format also
type(t1)
# list( is 1 dimensional representation of data which can be of mixed type and its mutable)
l1 = [10,20,30,40,10,60,90]
type(l1)
len(l1)

l1[3] 

# it will select 4th element because in python indexing start from zero
l1[3] = 9999
l1
l1.append(100)

# append will add the element at the end of the list
l1

l2 = [] # empty list

for i in range(1,50):
    l2.append(i*i)
    
l2
l2 = list(range(1,50))
l2[4]
l2[20]
l2[4:20]
# when we are using this colun it will go till 21  but it will not include 21

l2.count(2)

l3 = [1,1,1,1,1,1,1,10,4,4,4,4,12,13]
l3.count(4)

l3.remove(l3) # to remove the element
l3

l3.pop() # removes last element from the list
l3

l4 = list([2,3,4,5,'covid'])
l4

type(l4)

# object dictionary, is the represention of data in keys and values
# it is used to create the data frames
dict1 = {'name':'Mra', 'age':20, 'salary':1000} # pair of key and value

type(dict1)

dict1.keys()

dict1.values()
# a key can have multiple values but value can not have multiple keys
dict2 = {'name':('Mra', 'MRB', 'Mrc'), 'age':(20, 33, 44), 'salary':(1000, 2000, 3000)}

type(dict2)

dict2.keys()

dict2.values()

dict2 = {'name':('Mra', 'MRB', 'Mrc', 'Mrd'), 'age':(20, 33, 44, 23), 'salary':(1000, 2000, 3000, 1200)}

import pandas as pd

emply_details = pd.DataFrame(dict2)
emply_details
aa = set([2,3,4,4,5,6,6,6,6,67,89,90])

type(aa)

# print

a = 10
b = 20
print(a)
print(b)

print('value of a is ..',a)

# format printing

name  = 'Mrx'
salary = 10000
print('his name is  {}  and his salary  {}   is'.format(name, salary))

name  = 'Mrx'
salary = 10000
print('his name is  {}  and his salary  {}   is'.format(salary, name))

# input function
# it is use to take the input from the user
number = input('pass the value which you wish to enter : ')

number

number + 1000 # we get the error because number is string

type(number)

number1 = eval(input('pass the value which you wish to enter : '))
# eval function takes the input in that type only in which it is entered
# eval function helps in converting type of the function

type(number1)

number1 + 100
# eval will retain the data type which is being passed

# string
stng1 = 'covd19 is a big problem'

type(stng1)

len(stng1)

stng1 = '       covd19 is a big problem'
len(stng1)

stng2 = 'covid 19 is a big problem'

stng2.split()
stng2.split('i')

stng2.upper()# it convert all the words into the uppercase

stng3 = stng2.upper()
stng3
stng3.lower() # it will convert all the words into the lower case

t1 = [1,2,3]
t2 = [11,22,23]
t1*t2

import numpy as np

t1 = np.array(t1)
t2 = np.array(t2)
t1*t2

t1-t2# on array we can use maths function so above we have done that only 



