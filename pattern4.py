n = int(input("enter n:"))
for i in range(n): #for rows
    #print spaces
    print(" " * (n-i), end="")
    #print digit
    for j in range(1, 2 * i):
        print(j, end="")
    print() 