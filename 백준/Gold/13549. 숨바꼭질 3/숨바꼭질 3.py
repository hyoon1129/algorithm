from collections import deque
from os import times_result

n, k = map(int, input().split())

def bfs(n, k):
    queue = deque([(n, 0)]) # 위치, time
    visited = {}
    visited[n] = 0

    while queue:
        now, time = queue.popleft()

        if now == k:
            return time
        
        next = now * 2
        
        if next <= 100000 and next not in visited:
            queue.appendleft((next, time))
            visited[next] = time
        
        for next in [now-1, now+1]:
            if 0 <= next <= 100000 and next not in visited:
                queue.append((next, time+1))
                visited[next] = time + 1

    return 0

print(bfs(n, k))