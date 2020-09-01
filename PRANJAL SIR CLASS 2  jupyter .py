# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:55:48 2020

@author: sakshi
"""

# if statement
# else statement

i=9
if(i<10):
    print(i)
    print(i+1)
else:
    print('value is more than 10')
 
    
i = 2
if i<10:
    print(i)
    print(i+1)
else:
    print('value is more than 10')
    
    
# nested if else
city = input('enter the name of the city : ')

if city == 'pune':
    print('its our city')
elif city == 'mumbai':
    print('its capital of mh')
    print('its finicaial capital')
elif city == 'delhi':
    print('its capital of india')
else:
    print('this city is not in my data base.. please reenter')
    
# for loop
for i in range(1, 10):
    print(i)
    print(i*i)
    print('-----')
    
    
# while loop    
i = 1
while i < 10:
    print(i)
    i = i + 1   
    
# user defined function is define by [ 'def' ]
    
# creating a function
# a,b are arrgument
    

def add_num(a, b):
    res = a + b
    print(res)
    
add_num(123, 20) # calling function
# first value is maped to 'a' and the secand value is maped to 'b'

a # checking value of a
    
# user defined function
del(a)
del(b)
    

# creating a function
# a,b are arrgument

def add_num(a, b):
    res = a + b
    print(a)
    print(b)
    global res
    print(res) # res is the local variable if we will declaire it as global it will start working
    
    
add_num(123, 20) # calling function
# first value is maped to 'a' and the secand value is maped to 'b'

res

# Assignment
# create a user defined function which takes the input from the user and 
# identify wether its a even number or not
a = int(input('enter number : '))
def even_num(a):
    if a % 2 == 0:
        print(' {} number is even'.format(a))
    else:
        print(' {} number is odd'.format(a))
even_num()   
    
# or
def check_num():
    x = int(input("Enter a number"))

    if(x%2==0):
        print("EVEN!")
    else:
        print("ODD")
check_num()


# or
num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))
 
    
# or 
def check_num(a):
    if(a%2==0):
        print("Its a even number")
    else:
        print("Its an odd number")
check_num(eval(input("Enter the number")))    
    
    
    
    