from collections import deque
n, k = map(int, input().split())

if n == k:
    print(0)
    exit()
visited = [0 for i in range(100001)]
def bfs(start):
    queue = deque([(start, 0)])
    visited[start] = 1

    while queue:
        now, cnt = queue.popleft()

        move = [now-1, now+1, now*2]
        for m in move:
            if m == k:
                return cnt+1
            if 0<= m < len(visited) and not visited[m]:
                visited[m] = 1
                queue.append((m, cnt+1))

print(bfs(n))