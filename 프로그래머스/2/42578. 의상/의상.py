def solution(clothes):
    answer = 1
    
    closet = {}
    
    for name, kind in clothes:
        if kind in closet:
            closet[kind].append(name)
        else:
            closet[kind] = [name]
    
    cnt = []
    
    for key in closet.keys():
        cnt.append(len(closet[key])+1)
    
    if len(cnt) == 1:
        return cnt[0] - 1
    else:
        for i in range(len(cnt)):
            answer *= cnt[i]
    return answer-1