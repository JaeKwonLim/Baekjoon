n = int(input())
for i in range(n):
    lst = list(map(str, input().split()))
    aaa = ''
    count = int(lst[0])
    word = str(lst[1])
    for a in range(len(word)):
        aaa = aaa + count * word[a]
    print(aaa)    
