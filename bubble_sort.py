def insert():
    n = int(input("Enter numbers of elements you want to sort :"))
    num = list(range(n))
    print("Enter {0} numbers to be sorted ".format(n))
    for x in range(n):
        num[x] = int(input())
    return num


list = insert()
n = len(list)
for x in range(n-1):
    for y in range(n-x-1):
        if(list[y]>=list[y+1]):
            list[y],list[y+1]=list[y+1],list[y]
print(list)
