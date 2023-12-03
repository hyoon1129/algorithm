def dfs(i, n, computers):
    visited[i] = True

    for j in range(n):
        if computers[i][j] == 1 and visited[j] == False:
            dfs(j, n, computers)
    
def solution(n, computers):
    answer = 0
    global visited
    
    visited = [False] * n
    
    for i in range(n):
        if visited[i] == False:
            dfs(i, n, computers)
            answer += 1
    
    return answer