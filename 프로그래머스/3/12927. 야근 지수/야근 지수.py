import heapq
def solution(n, works):
    if n >= sum(works):
        return 0
    
    answer = 0
    works = [-w for w in works]
    
    heapq.heapify(works)
    
    
    for i in range(n):
        a = heapq.heappop(works)
        a += 1
        heapq.heappush(works, a)
        
    for i in works:
        answer += i**2
    
    
    return answer

'''
처음 코드
def solution(n, works):
    answer = 0
    
    works.sort(reverse = True)
    
    for i in range(n):
        if sum(works) == 0:
            return 0
        works[0] = works[0] - 1
        works.sort(reverse = True)
    

    
    for i in works:
        answer += i**2
    
    
    return answer'''