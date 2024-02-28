def solution(targets):
    answer = 0
    
    targets.sort(key = lambda x : x[1])
    
    
    now = targets[0][1]
    answer += 1
    
    for i in range(len(targets)-1):
        if now <= targets[i+1][0]:
            now = targets[i+1][1]
            answer += 1
            
    return answer