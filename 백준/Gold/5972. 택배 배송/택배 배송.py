import heapq
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

def dijkstra(graph, start):
    dist = [10**9] * len(graph)
    dist[start] = 0
    queue = [(0, start)]


    while queue:
        cost, node = heapq.heappop(queue)

        if cost > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor))
    return dist

dist = dijkstra(graph, 1)
print(dist[n])