n1 = int(input("ente the value of x:"))
match n1:
    case 0:
        print("the value is zero")
    case 1:
        print("the value is one")
    case 2:
        print("the value is two")
    case 4:
        print("the value is four")
    case _:
        print(n1)