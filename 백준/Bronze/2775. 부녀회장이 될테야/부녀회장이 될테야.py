t = int(input())
k = []
n = []
for i in range(t):
    k.append(int(input()))
    n.append(int(input()))

def solution(a, b):
    floor = [[0] * b for _ in range(a+1)]

    for i in range(b):
        floor[0][i] = i+1

    for i in range(1,a+1):
        for j in range(b):
            if j == 0:
                floor[i][j] = floor[i-1][j]
            else:
                floor[i][j] = floor[i][j-1] + floor[i-1][j]
    return floor[a][b-1]

for i in range(t):
    print(solution(k[i], n[i]))