n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][k] and matrix[k][j]:
                matrix[i][j] = 1
for row in matrix:
    print(' '.join(map(str, row)))