class car :
    def __init__ (self):
        self.acc = False
        self.brk = False
        self.cuk = False
    
    def start(self):
        self.acc = True
        self.cuk = True
        print("car is staring   now")

car1 = car()
car1.start()