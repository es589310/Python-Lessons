# while-continue
# num = int(input("Reqem daxil edin: "))
# i = 5
# while i <= num:
#     if i == 9:
#         i += 1
#         continue
#     print(f"Sayı: {i}")
#     i += 1

#FOR
# city = "Baku"
# city = 12 #tekrarlana bilmir
# for i in range(12):
#     print(i)


# fruits = [{"yellow" : "limon"},"alma",("alça","Qarpız")] # list
# # meyve = "ALMA" # string

# for fruit in fruits:
#     print(fruit)

# for i in ("Rehile","Sehra"):
#     print(i)

numbers = [2,4,6,8,10] #A4 kağız içində rəqəmlər və onun cəmini
total = 0 # əlavə A4 kağızı
# qələm for döngüsü əməliyyatı

# for number in numbers: #1 ci vərəqimdə olan rəqəmləri köçür 2 ci vərəqimə
#     total = total + number
#     print(total)


#Len 
# # fruit = ["apple","banan", "cherry"]
# fruit = "apple"
# for i in range(len(fruit)):
#     print(fruit[i])

# my_list = ["alma","alça","Qarpız","banan"]
# for i in range(len(my_list)): # range butun tipleri araligini verir
#     print(i)
# len daima=default olaraq int qaytarir 


# a = "2"
# b = "3"
# c = a , b 
# print(c)


list_1 = ["a","b","c"]
list_2 = [1,2,3]
# list_3 = list_1 + list_2
# print(list_3)


# x = input("dfbdfbdf")
# y = input("kjnskvnd")
# print(x, y)







# İstifadəçidən nömrə alaq
# n = int(input("Bir nömrə daxil edin: "))

# # Fibonacci ardıcıllığını hesablama
# a, b = 0, 1
# while a <= n:
#     print(a, end=" ")
#     a, b = b, a + b
#     if (a + b) < n:
#         print(f"{n} rəqəm fibonaççiyə uyğun deyil")

n = int(input("Bir nömrə daxil edin: "))
a,b = 0,1
fibonacchi = False

while a <= n:
    print(a, end=" ")
    if a == n:
        fibonacchi = True
    a,b = b, a + b

if not fibonacchi:
    print(f"\n{n} rəqəmi fibonaççiyə uyğun deyil.")


