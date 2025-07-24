import heapq

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
def dijkstra(n, matrix):
    dist = [[float('INF')] * n for _ in range(n)]
    dist[0][0] = matrix[0][0]
    heap = [(matrix[0][0], 0, 0)] # 비용, x, y

    while heap:
        cost, x, y = heapq.heappop(heap)

        if dist[x][y] < cost:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                next_cost = cost + matrix[nx][ny]
                if next_cost < dist[nx][ny]:
                    dist[nx][ny] = next_cost
                    heapq.heappush(heap,(next_cost, nx, ny))


    return dist[n-1][n-1]

num = 0
while True:
    n = int(input())
    if n == 0:
        break

    num += 1
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    print("Problem %d:" % num, dijkstra(n, matrix))
