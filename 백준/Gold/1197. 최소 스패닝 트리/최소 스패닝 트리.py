import sys
input = sys.stdin.readline

v, e = map(int, input().split())
parent = [i for i in range(v+1)] # 각자 부모 노드를 자기 자신으로 초기화

graph = []
for i in range(e):
    graph.append(list(map(int, input().split())))

graph.sort(key = lambda x : x[2]) # 가중치를 기준으로 정렬


def find_parent(node):
    if node != parent[node]:
        parent[node] = find_parent(parent[node])
    return parent[node]



def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b: # 작은 노드로 부모 노드 갱신
        parent[a] = b
    else:
        parent[b] = a
    return

answer = 0
for a,b,c in graph:
    if find_parent(a) != find_parent(b): # 두 노드가 사이클을 발생시키지 않으면
        answer += c
        union(a,b)
print(answer)