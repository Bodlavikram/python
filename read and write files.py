# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 15:24:05 2017

@author: vikram
"""
#writing to the file
with open("develop.txt","w") as file1: # "w" for writing to file
    file1.write("writing to the file") #writing data to the file
file1.close()

#reading from the file
with open("develop.txt","r") as file2: # "r" for reading from the file
    f=file2.read()  
    print("reading from the file")  #print statement
    print(f)
file2.close()  #close the file
    
    