num = int(input())

ssang = int(input())


graph = [[] * (num+1) for i in range(num+1)]

for i in range(ssang):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for i in range(num+1)]

def dfs(n):
    if visited[n]:
        return

    visited[n] = True
    global cnt
    cnt += 1

    for neighbor in graph[n]:
        dfs(neighbor)

cnt = 0
dfs(1)
print(cnt-1)