# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 23:41:44 2017

@author: vikram
"""
#addition function
def add(x,y):
    return x+y
#subtraction function
def sub(x,y):
    return x-y
#multiplication function
def mul(x,y):
    return x*y
#division function
def div(x,y):
    return x/y
print("select operation")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
#take input from the user
choice=input("enter choice(1/2/3/4):")

num1=int(input("enter the value for the first"))
num2=int(input("enter thee value for the second"))

if choice =='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice =='3':
    print(num1,"*",num2,"=",mul(num1,num2))
elif choice =='4':
    print(num1,"/",num2,"=",div(num1,num2))
    
    
