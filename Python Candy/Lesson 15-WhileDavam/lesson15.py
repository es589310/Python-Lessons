"""
number = int(input('Enter a number: ')) #start

# iterate until the user enters 0
while number != 0:
    print(f'You entered {number}.')
    number = int(input('Enter a number: ')) #continue

print('The end.')
"""


"""
#istfadeci adi ve parol ->  burda istifadəçi doğru məlumat yazarsa 
defistifadeci = "aydan"
defparol = "aydan123"

while True:
    user = input("Istifadeci adi ")
    parol = input("Istifadeci parolu ")
    if (user == defistifadeci) and (parol == defparol):
        print("Xoş gəlmişsiniz ", user)
        break # yazmasaq dogru bele olsa kodu dayandirmayacaq
    elif (user != defistifadeci) and (parol == defparol):
        print("Istifadəçi adı doğru deyil")
    elif (user == defistifadeci) and (parol != defparol):
        print("Istifadəçi parolu doğru deyil, parolu dəyişdirmək istəyirsinizmi?{B/X}")
        answer = input().upper()

        if answer == "B":
            new_parol = input("Yeni parolu daxil edin -> ")
            defparol = new_parol #iki beraber yox bir beraber
            print("Parol dəyişdi!")
        elif answer == "X":
            print("Bir daha yoxlayın..")
    else:
        print("bele bir istifadəçi mövcud deyil")

#şifrə doğru yazılmasa elə şifrədən versin və doğru cavabı versin?!
    """
"""
# !!!!
# while (n := len(input("Enter a string: "))) > 0:
#     print(f"Length of string: {n}")
"""



"""

# list_class = int(input("Reqemler: "))

# # i = 0
# while(i<10):
#     print("i-nin dəyəri - ", i) 
#     i = i + 1 

"""


"""
while True:
    user_1 = input("reqem yaz - proqramdan cixmaq isteseniz 'q'-nu basin: ")
    #eger q yazilsa
    if user_1 == 'q':
        break #proqrami dayandir
    elif user_1.isnumeric():
        print(f"Reqeminiz: {int(user_1)}")
    else:
        print("Herf yox reqem yaz")
"""

"""
parollar string verilir -> ishareler reqem herf
id - ler Integer(2.1 mlyrd.) ya da Long(9.2 katrlyon)
"""
"""
def_istifadeci = ""
def_parol = ""

while True:
    user = input("Istifadeci adi ")
    parol = input("Istifadeci parolu ")
    if (user == def_istifadeci) and (parol == def_parol):
        print("Xoş gəlmişsiniz ", user)
        break # yazmasaq dogru bele olsa kodu dayandirmayacaq
    elif (user != def_istifadeci) and (parol == def_parol):
        print("Istifadəçi adı doğru deyil")
    elif (user == def_istifadeci) and (parol != def_parol):
        print("Istifadəçi parolu doğru deyil, parolu dəyişdirmək istəyirsinizmi?{B/X}")
        answer = input().upper()

        if answer == "B":
            new_parol = input("Yeni parolu daxil edin -> ")
            def_parol = new_parol #iki beraber yox bir beraber
            print("Parol dəyişdi!", def_parol)
        elif answer == "X":
            print("Bir daha yoxlayın..")
    else:
        print("bele bir istifadəçi mövcud deyil")

"""

