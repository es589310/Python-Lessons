
# adam_tuple = ('adi daxil edin:','soyadi daxil edin:','yasi daxil edin:','ish_yerini daxil edin:')
# ad = input(adam_tuple[0])
# soyad = input(adam_tuple[1])
# yas = int(input(adam_tuple[2]))
# ish_yeri = input(adam_tuple[3])
# people = ad[0] , soyad[0] , str(yas[0]) , ish_yeri[0]
# print(people)

# #input default olaraq string 

#https://www.w3schools.com/python/python_tuples.asp

# Tuple 2 metodu var -> 
#Count
# my_tuple = (1,2,3,4,5,6,71,2,3,4,5,7,1)
# print(my_tuple.count(71)) #71-dən neçə dənə olduğunu bildirir
#Index
# print(my_tuple.index(71)) #71-in neçənci index-də olduğunu bildirir

# Tuple içindəki min() və max() nümunə

# sum_1 = sum(my_tuple)
# print(sum(my_tuple))
# print(sum_1)
# sum_1 = min(my_tuple)
# sum_1 = max(my_tuple)
# print(sum_1)


# tuple3 = (True, False, False)
# tuple3 = ( False)

# print(type(tuple3))

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-4])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-1:-4])

# thistuple = ("apple", "banana", "cherry")
# if "emin" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")
# else:
#   print("Bele bir obyekt yoxdu")

# x = ("apple", "banana", "cherry")
# y = list(x) # ["apple", "banana", "cherry"]
# y[1] = "kiwi" #["apple", "banana", "cherry"] => 1 => 
# x = tuple(y)

# print(x)


# class_1 = ("Rehile","Emin") #immutable
# # print(type(class_1))
# class_1_update = list(class_1)
# class_1_update.append("Resul")
# class_1 = tuple(class_1_update)
# print(class_1)

# i = 0
# i = i + 1 
# # i += 1
# print(i)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
#   "year": 2020,
  "colors": ["red", "white", "blue"]
}

# print(thisdict["brand"])
# print(len(thisdict))
print(thisdict)




