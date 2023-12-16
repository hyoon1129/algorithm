from collections import deque

def bfs(n, m, x, y, r, c, k):
    answer = []
    queue = deque()
    queue.append((x, y, 0, ""))
    
    dx = [1, 0, 0, -1] # 하 좌 우 상 (d l r u)
    dy = [0, -1, 1, 0]
    
    while queue:
        a, b, cnt, path = queue.popleft()
        # if cnt > k:
        #     return answer
        if [a,b] == [r,c] and (k-cnt)%2 != 0:
            return "imposible"
        elif [a,b] == [r,c] and k == cnt:
            return path
        
        # answer.sort()
        # if len(answer)>0 and answer[0][:len(path)] < path:
        #     continue
        
        for i in range(4):
            if i == 0:
                s = "d"
            elif i == 1:
                s = "l"
            elif i == 2:
                s = "r"
            else:
                s = "u"
                
            nx, ny = a+dx[i], b+dy[i]
            if 0<= nx < n and 0<= ny < m :
                if abs(nx-r) + abs(ny-c) + cnt + 1 > k :
                    continue
                queue.append((nx, ny, cnt+1, path + s))
                break
                
    return []
            
    
def solution(n, m, x, y, r, c, k):
    answer = ''
    global 거리
    
    
    x -= 1
    y -= 1
    r -= 1
    c -= 1
    
    거리 = abs(x-r) + abs(y-c)
    
    if 거리 > k:
        return "impossible"
    if (k-거리) % 2 != 0:
        return "impossible"
    
    return bfs(n, m, x, y, r, c, k)



    if li == []:
        return "impossible"
    else:
        li.sort()
        return li[0]