H, M = map(int, input().split())
mm = int(input())

A = (M + mm) // 60
B = (M + mm) % 60

if A >= 1 and H + A == 24:
    print(0, B)

elif A >= 1 and H + A > 24:
    print(H+A - 24, B)

elif A >= 1 and H + A < 24:
    print(H+A, B)

else:
    print(H, M + mm)