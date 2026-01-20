class student:
    def __init__(self, name ):
        self.name = name
        
    def __bala(self):
        print("private method")

    def welcome(self):
        self.__bala()
p1 = student("bala")
print(p1.welcome())