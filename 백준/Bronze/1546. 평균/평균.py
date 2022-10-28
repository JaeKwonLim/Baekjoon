n = int(input())  # 과목 수
lst = list(map(int, input().split()))
max_score = max(lst)
a = []
for i in range(n):
    a.append(lst[i]/max_score*100)

print(sum(a)/n)