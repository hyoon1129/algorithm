from collections import deque
n, m = map(int, input().split())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

x, y = 0, 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            x, y = i, j
            break

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

cnt_matrix = [[-1]*m for i in range(n)]

def bfs(x, y):
    visited = [[False]*m for _ in range(n)]
    queue = deque([(x, y, 0)])
    visited[x][y] = True
    cnt_matrix[x][y] = 0

    while queue:
        nx, ny, ncnt = queue.popleft()
        for i in range(4):
            tx, ty = nx+dx[i], ny+dy[i]
            if 0 <= tx < n and 0<= ty < m and not visited[tx][ty] and matrix[tx][ty] == 1:
                cnt_matrix[tx][ty] = ncnt + 1
                queue.append((tx, ty, ncnt+1))
                visited[tx][ty] = True

    return

bfs(x,y)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            cnt_matrix[i][j] = 0
for i in range(n):
    print(*cnt_matrix[i])