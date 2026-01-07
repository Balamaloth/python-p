#wrt a py program to dispaly *'s in right angle triangle form
# n = int(input("enter number of rowss:"))
# for i in range(1,n+1):
#     print("*"*i)


#how to commit all in vscode ctrl +shift +G

n = int(input("enter number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()


# n = int(input("Enter number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i+1): 
#         print("*",end=" ")
#     print() 