from collections import deque

n, m = map(int, input().split())

paper = []

for _ in range(n):
    paper.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[y][x] = True
    area = 0
    while queue:
        a, b = queue.popleft()
        area += 1

        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and paper[ny][nx] == 1:
                visited[ny][nx] = True
                queue.append((nx, ny))
    return area

visited = [[False]*m for _ in range(n)]


answer = 0
areas = []
for y in range(n):
    for x in range(m):
        if paper[y][x] == 1 and not visited[y][x]:
            areas.append(bfs(x, y, visited))
            answer += 1

print(answer)
print(max(areas) if areas else 0)