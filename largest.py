# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 23:56:27 2017

@author: vikram
"""
#program for largest of three numbers
#get the input from the user
num1=int(input("enter the num1 value"))
num2=int(input("enter the num2 value"))
num3=int(input("enter the num3 value")) 

if (num1>=num2) and (num1>=num3):
    largest=num1
elif (num2>=num1) and(num2>=num3):
    largest=num2
else:
    largest=num3
print("the largest number",num1,",",num2,"and",num3,"is",largest)