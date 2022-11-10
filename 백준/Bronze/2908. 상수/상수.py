lst = list(map(int, input().split()))
first = str(lst[0])
second = str(lst[1])

f = first[2] + first[1] + first[0]
s = second[2] + second[1] + second[0]

print(max(f,s))