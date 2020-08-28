from test import telebe
users = []
def melumatlariAl():
    input_ad = input("Ad :")
    input_soyad = input("Soyad :")
    input_username = input("Username :")
    input_password = input("Password :")
    print(input_ad)
    return [input_ad, input_soyad, input_username, input_password]

def qeydiyyat():
    userSayi = input("User sayini teyin et : ")
    for say in range(int(userSayi)):
        say += 1
        print(f"{say}-inci user qeydiyyati")
        users.append(telebe(*melumatlariAl()))


def melumatlariGoster():
    for user in users:
        user.show()


emr = input("Qeydiyyat prosesine baslamaq ucun 1 duymesine basin :")
if int(emr) == 1:
   qeydiyyat()