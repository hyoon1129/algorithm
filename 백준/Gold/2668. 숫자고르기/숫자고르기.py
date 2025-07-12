n = int(input())
li = []

for _ in range(n):
    li.append(int(input()))

num = [i for i in range(1, n+1)]

result = []

def dfs(current, start, visited, path):
    visited[current] = True
    path.append(current)

    next_node = li[current] - 1

    if not visited[next_node]:
        dfs(next_node, start, visited, path)
    elif next_node == start:
        result.extend(path)


for i in range(n):
    visited = [False] * n
    path = []
    dfs(i, i, visited, path)

result = sorted(set(result))
print(len(result))
for num in result:
    print(num+1)
