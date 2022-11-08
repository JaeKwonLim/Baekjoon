n = int(input())
lst = []

for i in range(1,n+1):
    a = str(i)
    if i < 100:
        lst.append(i)
    elif 1000 >= i >= 100:
        if int(a[2]) - int(a[1]) ==  int(a[1]) - int(a[0]):
            lst.append(i)

print(len(lst))