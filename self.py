class person:
    def __init__(self , name , age ):
        self.name = name 
        self.age = age 
    def greet(self):
       print("hello , my name is " + self.name + " and i am " + str(self.age) + " years old")
p1 = person("bala maloth", 22)
p1.greet()