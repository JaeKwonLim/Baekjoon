a = list(range(1, 31))
b = []
for i in range(28):
  b.append(int(input()))

print(min(set(a) - set(b)))
print(max(set(a) - set(b)))