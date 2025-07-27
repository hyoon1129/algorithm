import heapq

n = int(input())
m = int(input())

li = [[] for _ in range(n+1)]
dic = {}
for i in range(m):
    s, e, c = map(int, input().split())

    if s in dic:
        dic[s].append(e)
    else:
        dic[s] = [e]

    li[s].append((e, c))

s, e = map(int, input().split())

def dijkstra():
    dist = [float('INF')] * (n + 1)
    dist[s] = 0
    heap = [(0, s)] # 비용, 도시

    while heap:
        cost, city = heapq.heappop(heap)

        if dist[city] < cost:
            continue
            
        for v, c in li[city]:
            if dist[v] > cost + c:
                dist[v] = cost + c
                heapq.heappush(heap, (dist[v], v))

    return dist
dist = dijkstra()
print(dist[e])