n, m = map(int, input().split())

a = []
b = []
for i in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())
for i in range(m):
    b.append(list(map(int, input().split())))

answer = [[0] * k for i in range(n)]
for i in range(n):
    for j in range(k):
            for l in range(m):
                answer[i][j] += a[i][l] * b[l][j]
for row in answer:
    print(*row)