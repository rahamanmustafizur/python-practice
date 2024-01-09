eng_marks   =   int(input("enter marks of english:"))
math_marks  =   int(input("enter marks of math:"))
if    eng_marks   >   80   and    math_marks  >   80:
    print("you got grade A")
elif    eng_marks   >   80   or math_marks  >   80:
    print("you got grade B")
else:
    print("you got grade C")