import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 1

def dfs(v, graph, r):
    global cnt
    v[r]= cnt

    for neighbor in sorted(graph[r]):
        if not v[neighbor]:
            cnt += 1
            v[neighbor] = cnt
            dfs(v, graph, neighbor)
    return

visited = [0 for _ in range(n+1)]

dfs(visited, graph, r)
for i in range(1, n+1):
    print(visited[i])