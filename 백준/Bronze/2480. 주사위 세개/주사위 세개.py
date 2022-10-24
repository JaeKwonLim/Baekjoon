a, b, c = map(int, input().split())

if a == b:
    if a == b == c:
        print(10000 + a * 1000)
    else:
        print(1000 + a * 100)

elif a == c:
    if a == b == c:
        print(10000 + a * 1000)
    else:
        print(1000 + a * 100)

elif c == b:
    if a == b == c:
        print(10000 + a * 1000)
    else:
        print(1000 + c * 100)

else:
    number=[a,b,c]
    print(max(number) * 100)