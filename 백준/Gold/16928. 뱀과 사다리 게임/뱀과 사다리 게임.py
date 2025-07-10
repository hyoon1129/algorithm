from collections import deque
n, m = map(int, input().split())

ladders = {}

for _ in range(n):
    x, y = map(int, input().split())
    ladders[x] = y

snakes = {}

for _ in range(m):
    u, v = map(int, input().split())
    snakes[u] = v

def bfs():
    queue = deque([(1, 0)])
    result = []
    visited = [False for _ in range(101)]
    visited[1] = True
    while queue:
        node, cnt = queue.popleft()

        if node == 100:
            return cnt

        for i in range(1, 7):
            if i + node <= 100 and not visited[i+node]:
                new_node = i+node
                if node+i in ladders:
                    new_node = ladders[new_node]
                elif node+i in snakes:
                    new_node = snakes[new_node]
                queue.append((new_node, cnt + 1))
                visited[i+node] = True
    return

print(bfs())