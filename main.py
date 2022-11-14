#! /usr/bin/env python3

# Importing library
import math

# Requesting user input.  Taking in user input as a float
a = float(input("Please input value of side a: "))
b = float(input("Please input value of side b: "))
c = math. sqrt(a ** 2 + b ** 2)  # Mathematical equation, using a function

# Printing result
print(f"The length of the hypotenuse c is {c}")


# Using built-in functions to open a file
f = open("foobar.txt", "r")
print(f.read())
f.close()

# Use fib fuction
import fibo
from fibo import fib

num = int(input("Please input number to see fibonacci sequence: "))
fibo.fib(num)

# Import sys library
import sys

age = int(input("If you are too young this program won't run, please enter your age: "))

if age < 18:
    sys.exit("Age is less than 18")
else:
    print("You may enter this program")

# While loop 
count = int(input("Please enter another number: "))
while (count >= -1):
    print(count)
    count-=5
 
'''
 Mitigation in python in my terms, is the evaluation of libraries and such for 
 potential exploits and vulnerablities.  For example, certain Python versions is 
 RHEL and RHSCL are vulnerable to Web Cache Poisoning through the urllib query
 string parsing functions by using a vector called parameter cloaking.  In today's 
 climate any vulnerablity or exploit is a potential risk of bad actors getting your 
 information or access to documents that should be private, even if the exploit takes
 15 years to find.
'''   
    
    
    
          