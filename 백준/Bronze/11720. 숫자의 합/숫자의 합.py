count = int(input())
n = input()
a = 0

for i in range(count):
    a = a + int(n[i-1])

print(a)