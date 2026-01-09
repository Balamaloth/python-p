x = "bala"

def myfunc():
    global x
    x = "krishna"

myfunc()

print("this is "+ x)
print("this is also "+ x)