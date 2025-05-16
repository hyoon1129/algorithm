from collections import deque

n = int(input())

a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start, end, graph):
    visited = []
    queue = deque([(start, 0)])
    while queue:
        node, cnt = queue.popleft()
        if node not in visited:
            if node == end:
                return cnt
            visited.append(node)
            for neighbor in graph[node]:
                queue.append([neighbor, cnt + 1])

    return -1

print(bfs(a, b, graph))