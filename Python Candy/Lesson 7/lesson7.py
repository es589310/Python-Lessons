# Sort List metods
# sort()
# fruit_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
# fruit_list.sort()
# print(fruit_list)
# num_list = [2,3,52,3,5,7,3433,1,3]
# num_list.sort() #sort üçün variable-a əks eləmək olmaz
# print(num_list)

#!# num_list.sort() #sort üçün variable-a əks eləmək olmaz

# num_list = [2,3,52,3,5,7,3433,1,3]
# num_list.sort(reverse=True)  #sort üçün variable-a əks eləmək olmaz
# num_list.reverse()

# print(num_list)

#??????
# fruit_list = ["oraNge", "mango", "Kiwi", "pineapplE", "banAna"]
# fruit_list.sort(key=str.lower)
# print(fruit_list)


# Join list -> birlesmek qosmaq
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

# a = 1.3
# b = 2
# c = a + b 
# print(c)

# #extend - genisletmek
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# # list1.extend(list2)
# list2.extend(list1)

# print(list2)


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])
# print(thislist[-2])

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

"""
List -> mutable []
Tuple(Dəst) -> immutable ()  
"""

# Tuple 2 metodu var -> 
#Count
my_tuple = (1,2,3,4,5,6,71,2,3,4,5,7,1)
print(my_tuple.count(71))
print(my_tuple.index(71))

# tuple_1 = (1,2,3)
# print(tuple_1)
# tuple_2 = (1) #-> int
# tuple_3 = (1,) #-> tuple
# print(type(tuple_2))
# print(type(tuple_3))



    

