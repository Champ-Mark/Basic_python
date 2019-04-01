n = int(input("Enter numbers of elements you want to sort :"))
num = list(range(n))
print("Enter {0} numbers to be sorted ".format(n))
for x in range(n) :
    num[x] = int(input())
for x in range(n) :
    for y in range(x,n):
        if(num[x]>=num[y]) :
            num[x],num[y]=num[y],num[x]

print(num)