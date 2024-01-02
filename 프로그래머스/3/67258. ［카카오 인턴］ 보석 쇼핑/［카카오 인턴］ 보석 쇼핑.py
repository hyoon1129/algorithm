def solution(gems):
    n = len(gems) 
    answer = [0, n-1]
    dic = {gems[0]:1}
    kind = len(set(gems)) # 보석 종류
    left, right = 0, 0 # 투포인터
    
    while left < n and right < n:
        if len(dic) < kind:
            right += 1
            
            if right == n:
                break
            
            if gems[right] not in dic:
                dic[gems[right]] = 1
            else:
                dic[gems[right]] += 1
                
        else:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            else:
                dic[gems[left]] -= 1
                if dic[gems[left]] == 0:
                    del dic[gems[left]]
                left += 1

    return [answer[0]+1, answer[1]+1]
                
        
    