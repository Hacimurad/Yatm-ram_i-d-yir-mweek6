from test import oyuncular
global users
users = []

def Melumatlaral():
    in_ad = input("Isdifadeci adi:")
    in_soyad = input("Isdifadeci soyadi:")
    in_email = input("Isdifadeci email:")
    in_password = input("Isdifadeci password:")
    return [in_ad,in_soyad,in_email,in_password]

def qeydiyyat():
    oyuncusayiteyin = input("Oyuncularin sayini sec:")
    for say in range(int(oyuncusayiteyin)):
        print(f"{say}-inci oyuncunun Qeydiyyat")
        users.append(oyuncular(*Melumatlaral()))
def oyuncularigosder():
    for oyuncu in users:
        oyuncu.show()

emr=input("Qeydiyyat baslatmaq isdeyirsense 1-bas:")
if int(emr)==1:
   qeydiyyat()
emr2=input("Butun oyunculari gosder")
if int(emr2)==2:
    oyuncularigosder()

ad=input("Isdefadeci adina gore axdar:")
def adagoregosder(ad):
    for oyuncu in users:
      if oyuncu.ad == ad:
         oyuncu.show()
      else:
          print("Yalniz ad girdiniz")
adagoregosder(ad)

#Alinmirrr
'''def showUserByName():
if len(users) == 0:
        print("There is no user in the system!")
    else:
        longestName = ""
        for user in users:
            if len(user.ad) > len(longestName):
                longestName = user.ad
        showUserByName(longestName)'''



'''soyad=input("Soyadinda ov varsa gosder")
def soyadinda_ov_olan():
    for oyuncu in users:
        if ov in oyuncu.in_soyad:
          print(f"Isdifadecinin soyadi{oyuncu.soyad}")'''






