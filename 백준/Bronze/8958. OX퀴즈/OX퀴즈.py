n = int(input())

for i in range(n):
    lst = list(input())
    total_score = 0
    again = 0
    for i in range(len(lst)):
        if lst[i] == 'O':
            again += 1
            total_score += again
        else:
            again = 0
    print(total_score)