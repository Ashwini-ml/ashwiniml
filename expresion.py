n1=int(input("enter the n1"))
operator=input("enter operator(+,-,/,%,*,):")
n2=int(input("enter the n2"))


if operator == "+":
    print(n1+n2)
elif operator == "-":
    print(n1-n2)
elif operator == "/":
    print(n1/n2)
elif operator == "%":
    print(n1%n2)
elif operator == "*":
    print(n1*n2)
else:
    print("invalid operator")

