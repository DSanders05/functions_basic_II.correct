#1. Countdown
def countdown(num):
    something = []
    for i in range(num,-1,-1):
        something.append(i)
    print(something)
countdown(12)

#2. Print and Return-Create a function that will receive a list with two numbers. Print the first value and return the second.
list = ("yes","no")
def createLst(list=list):
    print(list[0])
    return list[1]
list2 = [1,2]
createLst()
createLst(list2)

#3.First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def createList(some_list):
    return some_list[0] + len(some_list)
print(createList([4, 8, 3, 2]))

#4.Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def createList(some_list):
    if(len(some_list)<2):
        return False
    new_list= []
    for v in range(len(some_list)):
        if (some_list[v]>some_list[1]):
            new_list.append(some_list[v])
    if(len(new_list)<1):
        return "None"          
    return new_list

print(createList([2]))
print(createList([1,5]))
print(createList([5,2,3,7,1,2,4]))

#5.This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def size(size, value):
    new_list = []
    for i in range(size):
        new_list.append(value)
    return new_list

print(size(4,7))