#Dictionary Task2
# dict_1 = {
#     "Rehile":17,
#     "Rehile":18,
#     "Rehile":19
# }
# print(dict_1)

#Setting -> add

# set_1 = {1,2,3,4,56,7}
# # set_1.pop()
# # print(set_1)
# mylist = {"kiwi", "orange"}
# set_1.update(mylist)
# print(set_1)

#For ile
# thisset = {("apple",5), ("banana",8), ("cherry",4)}

# for x in thisset:
#   print(x)
# print(("banana",8) in thisset)
# print(("cherry",4) not in thisset)

# thisset.remove(("cherry",4)) 
# print(thisset)
#throws xətası qaytarmır -> compile ve runtime errors
# thisset.discard(("fındıq")) #-> throws errosdan uzaqdir
# print(thisset)

# del thisset
# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# del thisset #NameError: name 'thisset' is not defined
# # thisset.clear() #icindekileri silmek icin
# print(thisset)


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# set3 = set1.union(set2) #union elave bir variable isteyir
# set3 = set1 | set2 # | -> union
# print(set3)

set1 = {"apple", "banana", "cherry",}
set2 = {"google", "microsoft", "apple"}
#intersection = kesishme -> &
# set3 = set1.intersection(set2)
# set3 = set1 & set2
# set3 = set1.intersection_update(set2)
# set3 = set1.difference(set2) # -
# set3 = set2 - set1 
# print(set3)

# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}

# set3 = set1.intersection(set2)

# print(set3)



#Dictionary
thisdict = {
  "brand": "BMW",
  "model": "F10",
  "year": 2018
}



# new_model = thisdict.get("model")
# new_model = thisdict.keys()
# new_model = thisdict.values()

# print(new_model)
# print(thisdict["year"])
