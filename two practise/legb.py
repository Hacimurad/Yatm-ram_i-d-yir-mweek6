#miras verirse Base klass olur
class Parent:
    def __init__(self,ad,soyad):
        self.name =ad
        self.surname =soyad
    def show(self):
        print(f"{self.name},{self.surname}")
#miras alirsa derived klassdi
class Child(Parent):
    def __init__(self,ad,soyad,role):
        Parent.__init__(self,ad,soyad)
        self.role = role

    def show(self):
        print(f"{self.name},{self.surname},{self.role}")
user=Parent("samir","Kerimov")
user.show()
xuser=Child("dfd","ddd","fds")
xuser.show()
