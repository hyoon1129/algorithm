def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    dic = {}
    
    for num in tangerine:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
            
    li = []      
    for cnt in dic.keys():
        li.append(dic[cnt])
    li.sort(reverse = True)
    
    a = 0
    i = 0
    while a < k:
        a += li[i]
        answer += 1
        i += 1
    return answer