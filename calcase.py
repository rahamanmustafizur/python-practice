num1 = int(input("enter the numbet:"))
num2 = int(input("enter the number:"))
operator = input("enter operator:")
match operator:
    case "+":
        print("the sum is ",num1 + num2)
    case "*":
        print("the multiply is ",num1 * num2)