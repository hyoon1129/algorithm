def solution(n, costs):
    answer = 0
    global parent
    parent = [i for i in range(n)] # 각자 부모를 자기 자신으로 초기화
    costs.sort(key = lambda x : x[2]) # cost 기준으로 오름차순 정렬
    
    for cost in costs:
        if find_parent(cost[0]) != find_parent(cost[1]): # 사이클이 생기지 않음
            answer += cost[2]
            union(cost[0], cost[1])
            
    return answer

def find_parent(node):
    if node != parent[node]:
        parent[node] = find_parent(parent[node])
    return parent[node]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return 