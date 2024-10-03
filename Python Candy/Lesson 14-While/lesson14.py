#task 1
# name = input("Adınız: ")
# age = int(input("Yaşınızı qeyd edin: "))
# nationaly = input("Hansı ölkə vətəndaşısınız?: ")

# if age >= 18:
#     if nationaly == "Azərbaycan":
#         print(f"{name}, siz seçkilərdə iştirak edə bilərsiz!")
#     else:
#         print(f"{name}, siz xarici vətəndaşsınız, iştirak edə bilərməzsiniz!")
# elif age < 18:
#     print(f"{name}, siz seçkilərdə iştirak edə bilməzsiniz!")

    
#task 2
# bal = int(input("Balı daxil edin: "))

# if (bal >= 90) and (bal <= 100):
#     print("A")
# elif (bal >= 80) and (bal <= 89):
#     print("B")
# elif (bal >= 70) and (bal <= 79):
#     print("C")
# elif (bal >= 60) and (bal <= 69):
#     print("D")
# else:
#     if (bal >= 30) and (bal <= 59):
#         print("Dərsdən şərtli olaraq keçdiniz!")
#     else:
#         print("Biyabırçılıqdır!")

#Task 3

# user = "rehile"
# pasword = "123456"

# user_terminal = input("Istifadəçi adınızı qeyd edin: ")
# pasword_terminal = input("Şifrənizi qeyd edin: ")

# if (user == user_terminal) and (pasword == pasword_terminal):
#     print("Giriş təyin olundu!")
# else:
#     if (user != user_terminal) and (pasword == pasword_terminal):
#         print("User səhvdir!")
#     elif (user == user_terminal) and (pasword != pasword_terminal):
#         print("Parol səhvdir!")
#     else:
#         print("Belə bir istifadəçi mövcud deyil!")


#WHILE
"""
dövr dəyişəni
while (məntiq cümləsi):
    ediləcək əməliyyat
    artırma əməlliatı -> i = i + 1
"""

# while True:
#     print(23)
#ctrl + C

# thislist = ["Alma","Armud","Heyva"]
# i = 0 # result -> yerine qoyacaq
# while i < len(thislist):
#     print(thislist[i]) #"ALma"
#     i += 1

# i = 0 #0 1  2 3
# while (i < 10):
#     i += 1 # 1 2 3 4 5
#     print("i = ", i) #0 1

# while True:
#     print("i = 10")
#     break


while True:
    user_1 = input("reqem yaz - proqramdan cixmaq isteseniz 'q'-nu basin: ")
    #eger q yazilsa
    if user_1 == 'q':
        break #proqrami dayandir
    elif user_1.isnumeric():
        print(f"Reqeminiz: {int(user_1)}")
    else:
        print("Herf yox reqem yaz")

