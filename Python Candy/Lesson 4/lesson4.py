#F string
# name = "Emin"
# surname = "Panahov"

# print(f"{name}     {surname}")

# num1 = 23
# num2 = 26
# print(f"{num1} + {num2} = {num1 + num2}")

# print({num1} + {num2} = {num1 + num2}) #error

#Format metodu

# name = "Emin"
# surname = "Panahov"
# print("Ad {0} - Soyad {1}".format(name, surname))

# /n
# print("Neque porro quisquam est qui dolorem ipsum \nquia dolor sit amet, consectetur, adipisci velit...")

# print("Neque porro quisquam est qui dolorem ipsum", end=(". "))
# print("Neque porro quisquam est", "qui dolorem ipsum ijnfisnfisf", sep=("---"))

# Input funksiya
# -dinamikdir, default stringdir

# name = input("Adı daxil edin: ")
# surname = input("Soyadı daxil edin:")
# print( name , "", surname)

# age1 = int(input("Eminin yasi: "))
# age2 = int(input("Rehilenin yasi: "))
# print(age1 + age2)

#Variable
"""
x = "4 katlet"
# x = "aş" 
print(x)
x = "aş" #boshqabin kenarinda
"""
#variable text type
#camel case=()
myVariableName = "baş hərfi balaca digərləri böyük"
#Pascal case
MyVariableName1 = "butun boyukle yazilir"
#Snake Case
_my_variable_name_ = "ilan kimi qivrilan variable yazilisi" 

#icaze yoxdu, compile error verir ve SyntaxError verir
# 1m3yv3a5r = 5 #başda reqem yazmaq olmaz
# print(2myvar)

# my-var = 5 # defisden istifadeye icaze vermir
# print(my-var) 

# my var = 5 # boshluq yazmaghada icaze vermir
# print(my var)

# x = 2
# y = 2
# z = 2
# x = y = z = 2
# print(x + y + z)

# fruits = ["alma","ciyelek","armud","banan"]
# x,y,z,a = fruits
# print(x)
# print(y)
# print(z)
# print(a)

# x = 23
# def myFunction():
#     print("Uğurlu rəqəmim ", x)

# myFunction()

#Sequence(Sıra) Types
"""
list() => [] -> list bir tipdir -> oz metodları
"""
# my_list = [123]
# print(type(my_list))

"""
tuple() => immutable => hecneyi deyismeyib => () => 2 metodu
"""
# my_tuple = (1,2,3,4)
# print(type(my_tuple))
# print(my_tuple)

"""
set-> setting(ayarlamaq) => {} => temel ayarlamalara icaze verir => sırasız
"""
# my_set ={1,2,3,4,5,3,54,5,6,43}
# print(my_set)
# print(type(my_set))

"""
dict => dictionary(lughet) => {key = value} => siralidir 
"""
# my_dict = {
#     'key' : 5
# }
# print(my_dict)
# print(type(my_dict))

#Boolen data type
"""
menfi ve musbet olan her sey = 1 = True
sadece neytral = 0 = False
qisaltma bool
"""
# my_bool = True
# print(type(my_bool))
# my_bool = False
# print(type(my_bool))


"""



"""
line1 = "Nâzım Hikmet vatan hainliğine devam ediyor hâlâ"
line2 = "Amerikan emperyalizminin yarı sömürgesiyiz, dedi Hikmet"
line3 = "Nâzım Hikmet vatan hainliğine devam ediyor hâlâ"
line4 = "Bir Ankara gazetesinde çıktı bunlar"

# poema = f"{line1},\n{line2},\n{line3},\n{line4}"
print(line1,line2,line3,line4)
# print(poema)