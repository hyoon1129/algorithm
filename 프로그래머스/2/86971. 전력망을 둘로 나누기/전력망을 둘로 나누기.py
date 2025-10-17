from collections import deque
def solution(n, wires):
    answer = 10**9
    
    def make_graph(wire):
        graph = [[] for _ in range(n+1)]

        for v1, v2 in wires:
            if [v1, v2] == wire or [v2, v1] == wire:
                continue
            graph[v1].append(v2)
            graph[v2].append(v1)
        return graph
    
    def bfs(graph, start):
        queue = deque([start])
        visited = [False for _ in range(n+1)]
        visited[start] = True
        cnt = 1
        
        while queue:
            now = queue.popleft()
            
            for next_node in graph[now]:
                if not visited[next_node]:
                    visited[next_node] = True
                    cnt += 1
                    queue.append(next_node)
        return cnt
        
    for wire in wires:
        graph = make_graph(wire)
        cnt1 = bfs(graph, wire[0])
        cnt2 = n-cnt1
        answer = min(answer, abs(cnt1-cnt2))

    
    return answer