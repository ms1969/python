l = []
n = int(input())
i = 0
sum = 0
for i in range(n):
    l.append(list(map(int, input().split())))
for i in range(n):
    j = 0
    for j in range(n):
        if j == i:
            sum += l[i][j]
print(sum)

