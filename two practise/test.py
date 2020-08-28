
class oyuncular:
    def __init__(self,_ad,_soyad,_email,_password):
        self.ad=_ad
        self.soyad=_soyad
        self.email=_email
        self.password=_password
    def show(self):
        print(f"Isdifadeci adi:{self.ad},Isdifadeci soyadi:{self.soyad},Email:{self.email},Password:{self.password}")

