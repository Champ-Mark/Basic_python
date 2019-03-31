a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if a>b and a>c:
    print("{0} the first is greatest ".format(a))
elif (b>a) and (b>c) :
    print("{0} the second is greatest ".format(b))
else:
    print("{0} the third is greatest".format(c))