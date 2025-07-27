import heapq

n = int(input())    # 도시 개수
m = int(input())    # 버스 개수

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))  # u에서 v로 가는 비용 cost

start, end = map(int, input().split())

def dijkstra(start):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0

    pq = [(0, start)]  # (현재까지 비용, 노드 번호)

    while pq:
        curr_cost, curr_node = heapq.heappop(pq)

        # 이미 더 짧은 경로가 있다면 무시
        if distance[curr_node] < curr_cost:
            continue

        for neighbor, edge_cost in graph[curr_node]:
            new_cost = curr_cost + edge_cost

            if distance[neighbor] > new_cost:
                distance[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    return distance

dist = dijkstra(start)
print(dist[end])