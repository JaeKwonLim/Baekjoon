X = int(input())
n = int(input())
pp = []

for i in range(n):
    a, b = map(int, input().split())
    c = a * b
    pp.append(c)
    n = n - 1
    if n == 0:
        if sum(pp) == X:
            print('Yes')
        else:
            print('No')