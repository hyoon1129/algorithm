import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(now, visited):
    visited[now] = True

    for neighbor in graph[now]:
        if not visited[neighbor]:
            dfs(neighbor, visited)
    return

visited = [False for _ in range(n+1)]
cnt = 0

for i in range(1,n+1):
    if not visited[i]:
        dfs(i, visited)
        cnt += 1
print(cnt)
