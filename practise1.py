Gameusers=[]
class Plays:
    def __init__(self,_ad,_soyad,_username):
        self.ad=_ad
        self.soyad=_soyad
        self.username=_username

    def showData (self):
            print(f"Name:{self.ad},Surname:{self.soyad},Usersname:{self.username}")

def gamercreat():
    Ad = input("Name:")
    Soyad = input("Surname:")
    Username = input("Usersname:")
    gamers = Plays(Ad, Soyad, Username)
    Gameusers.append(gamers)
i=0
while i<5:
  gamercreat()
  i+=1

for Plays in Gameusers:
    Plays.showData()





