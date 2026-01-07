# wrt a progrsam to display *'s in triangle form

n = int(input("enter number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("* "*i)