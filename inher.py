class car:
    color = "red"
    @staticmethod
    def start():
        print("car is starting now ")

    @staticmethod
    def stop():
        print("car is stoping now ")

class toyotacar(car):
    def __init__(self , name):
        self.name = name 

car1 = toyotacar("lambogini")
        
car2 = toyotacar("ferrari")
print(car1.color)
print(car2.start())