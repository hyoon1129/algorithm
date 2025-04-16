from collections import deque
n, m = map(int, input().split())

campus = []
for i in range(n):
    campus.append(list(input()))

for i in range(n):
    for j in range(m):
        if campus[i][j] == "I":
            x, y = i, j

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

visited = [[False] * m for i in range(n)]


def bfs(x, y, visited):
    answer = 0
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            xx, yy = cx+dx[i], cy+dy[i]
            if 0 <= xx < n and 0 <= yy < m and not visited[xx][yy]:
                if campus[xx][yy] == "P":
                    answer += 1
                if campus[xx][yy] == "X":
                    continue
                queue.append((xx, yy))
                visited[xx][yy] = True
    return answer

count = bfs(x, y, visited)
if count == 0:
    print("TT")
else:
    print(count)