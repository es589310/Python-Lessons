#Boolean -> bool
# a = 23 > 14
# print(type(a)) 
# b = 16 < 12
# print(b)
#1 və 0 qaytarır

# a = 200
# b = 333

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

"""  
print(bool("Hello"))
print(bool(15))
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
"""

#Operators
# x = 5
# y = 2

# print(x % y)
# print(x ** y)
# print(x / y)
# print(x // y)

# Assignment Operator
# x = 4
# x = x + 3 
# y += 3
# print(y)
#https://www.w3schools.com/python/python_operators.asp

# x = 7

# x &= 3

# print(x)


# List Types
# https://www.w3schools.com/python/python_lists.asp

# a = [1,2,3,4,5,6,7]
# a = list((1,2,3,4,5))
# print(a)
# print(type(a))
# print(a)
#mutable -> prosesin icinde deyismesine

# Add List metods:
# insert
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "kiwi")
# append
# thislist.append("kiwi") #listin sonuna
# extend
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# extend tuple
# thistuple = ("kiwi", "orange") 
# thislist.extend(thistuple)

# print(thislist)

# Remove List metod
# remove
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana") # case icinde 1 element
# pop
# thislist.pop() #tek olanda sonuncu indeksi silir
# thislist.pop(1)
# del
# del thislist[1]
# clear
# thislist.clear()

# print(thislist)


# Copy a List
# copy()

# fruits = ["apple", "banana", "cherry"]
# fruit_1=fruits.copy()
# list()
# fruit_1 = list(fruits)

# fruit_1 = fruits

# print(fruit_1)



ballar = [85, 92, 78, 90, 88, 76, 95, 89, 91]
ballar.sort(reverse=True)  # Sort in descending order
print(ballar[0])  # Print the highest value after sorting













"""
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

"""

