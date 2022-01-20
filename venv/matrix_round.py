l = []
s = input()
n = list(map(int, s.split()))[0]
m = list(map(int, s.split()))[1]
i = 0
for i in range(n):
    l.append(list(map(int, input().split())))
for i in range(n - 1, -1, -1):
    j = 0
    for j in range(m):
        print(l[i][j], end=' ')
    print()
