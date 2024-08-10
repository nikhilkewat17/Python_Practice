class Grandfather:
    def height(self):
        print("Tall")
class Father(Grandfather):
    def skills(self):
        print("Programming in Python")
class Son(Father):
    def skills(self):
        super().skills()
        print("Fitnees Addict")

son = Son()
son.height()
son.skills()