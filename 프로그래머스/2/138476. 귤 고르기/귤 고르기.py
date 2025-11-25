def solution(k, tangerine):
    answer = 0
    
    tangerine = sorted(tangerine)
    
    dic = {}
    
    for i in range(len(tangerine)):
        if tangerine[i] in dic:
            dic[tangerine[i]] += 1
        else:
            dic[tangerine[i]] = 1
            
    li = sorted(list(dic.values()), reverse = True)
    
    temp = 0
    i = 0
    
    while temp < k:
        answer += 1
        temp += li[i]
        i += 1
    
    return answer