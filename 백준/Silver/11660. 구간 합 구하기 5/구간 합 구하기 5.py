n, m = map(int, input().split())

matrix = []
matrix.append([0]*(n+1))
for i in range(n):
    matrix.append([0] + list(map(int, input().split())))

tc = []
for i in range(m):
    tc.append(list(map(int, input().split())))

prefix = [[0] * (n+1) for i in range(n+1)]
prefix[1][1] = matrix[1][1]

for i in range(1, n+1):
    prefix[1][i] = prefix[1][i-1] + matrix[1][i]
    prefix[i][1] = prefix[i-1][1] + matrix[i][1]


for i in range(1, n+1):
    for j in range(1, n+1):
        prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + matrix[i][j]

for x1, y1, x2, y2 in tc:
    x1 -= 1
    y1 -= 1
    print(prefix[x2][y2]-prefix[x2][y1]-prefix[x1][y2]+prefix[x1][y1])


