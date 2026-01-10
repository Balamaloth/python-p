for r in range(0,5):
    for s in range(0,5-1-r):
        print(" ",end=" ")
    for c in range(0,r+1):
        print("*",end=" ")
    print("")