class student:
    def __init__(self, name , markd):
        self.name = name
        self.markd = markd
        print("student details and marks")
s1 = student("bala",95)
print(s1.name,s1.markd)

s2 = student("maloth", 100)
print(s2.name,s2.markd)