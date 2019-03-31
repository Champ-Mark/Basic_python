n = int(input("Enter the number you want to Reverse :"))
num,rnum,i =n,0,0
while n:
    rem = n%10
    n = int(n/10)
    rnum = rnum*10+rem
    i=i+1
print("Reverse of "+repr(num)+ " is " +repr(rnum))
print("Number of digits are {0}".format(i))