from collections import deque

n, m, v = map(int, input().split())


graph = {}

for _ in range(m):
    a, b = map(int, input().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]


def bfs(graph, v):
    result = [v]
    queue = deque([v])
    visited = [False for _ in range(n+1)]
    visited[v] = True

    while queue:
        node = queue.popleft()

        for neighbor in sorted(graph.get(node, [])):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                result.append(neighbor)
    return result


def dfs(graph, v):
    result = []
    visited = [False for _ in range(n + 1)]
    stack = [v]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            result.append(node)
            for neighbor in sorted(graph.get(node, []), reverse = True):
                if not visited[neighbor]:
                    stack.append(neighbor)
    return result

print(*dfs(graph, v))
print(*bfs(graph, v))