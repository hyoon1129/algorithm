import sys
input = sys.stdin.readline


n, m = map(int, input().split())

matrix = []
parent = [i for i in range(n+1)]

for i in range(m):
    matrix.append(list(map(int, input().split())))


def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


matrix.sort(key = lambda x : x[2])

answer = []

for a, b, cost in matrix:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer.append(cost)

print(sum(answer)-max(answer))