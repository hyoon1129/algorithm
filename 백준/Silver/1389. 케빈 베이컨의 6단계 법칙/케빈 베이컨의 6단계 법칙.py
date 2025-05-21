from collections import deque
n, m = map(int, input().split())

li = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)

def bfs(start):
    dist = [0] * (n+1)
    queue = deque([start])
    visited = [False] * (n+1)
    visited[start] = True

    while queue:
        x = queue.popleft()
        for neighbor in li[x]:
            if not visited[neighbor]:
                visited[neighbor] = True
                dist[neighbor] = dist[x] + 1
                queue.append(neighbor)
    return sum(dist)

kevin = [0] * (n+1)
for i in range(1, n+1):
    kevin[i] += bfs(i)

min_value = min(kevin[1:])
for i in range(1, n+1):
    if kevin[i] == min_value:
        print(i)
        break