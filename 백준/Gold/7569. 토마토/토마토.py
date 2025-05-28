from collections import deque
m, n, h = map(int, input().split()) # 가로, 세로, 높이

tomato = [[] for _ in range(h)]

for i in range(h):
    for j in range(n):
        tomato[i].append(list(map(int, input().split())))

dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
cnt = -1
def bfs():
    global queue, cnt

    while queue:
        for _ in range(len(queue)):
            z, x, y = queue.popleft()
            for i in range(6):
                nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
                if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                    if tomato[nz][nx][ny] == 0:
                        tomato[nz][nx][ny] = 1
                        queue.append([nz, nx, ny])
        cnt += 1
    return cnt


queue = deque()
yes_tomato = 0
no_tomato = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                yes_tomato += 1
                queue.append([i, j, k])
            elif tomato[i][j][k] == -1:
                no_tomato += 1

if yes_tomato + no_tomato == h*m*n:
    print(0)
    exit()

bfs()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                print(-1)
                exit()
print(cnt)