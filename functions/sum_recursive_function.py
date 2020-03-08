# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 01:56:58 2020

@author: Debugger
"""

#function for recursively summing all elements in the list
def sum_recursive(lis):
    # checking base case weather list length is greater than 1 or not
    if(len(lis)>1):
        #if list length is greater than 1 it will sum first element and send other elements to recursive function
        return lis[0] + sum_recursive(lis[1:])
    #if list length is equal to 1 return that element
    return lis[0]

# list of numbers
numbers = [1,2,3,4,5,6,7,8]
# fucntion calling inside print function
print(sum_recursive(numbers))