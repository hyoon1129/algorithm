def solution(distance, rocks, n):
    answer = 0
    
    rocks.append(distance)
    rocks.sort()
    
    start, end = 1, distance
    
    while start<=end:
        mid = (start+end) // 2
        
        deleted = 0 # 제거된 돌
        current = 0 # 기준이 되는 돌
        min_distance = 10**9
        
        for rock in rocks:
            
            if rock - current < mid:
                deleted += 1
            else:
                current = rock
                min_distance = min(mid, rock - current)
                
            if deleted > n:
                break
        
        if deleted > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer


# 