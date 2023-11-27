def solution(dirs):
    answer = 0
    now = (0,0)
    dic = {}
    
    for w in dirs:
        target = move(now, w)
        if target != now:
            if now not in dic:
                if target not in dic or now not in dic[target]:
                    dic[now] = []
                    dic[now].append(target)
            else:
                if target not in dic or now not in dic[target]:
                    if target not in dic[now]:
                        dic[now].append(target)
            
                    
            now = target
            
    for i in dic.values():
        answer += len(i)
    
    return answer

# UDLRL

def move(start, w):
    target = ()
    x, y = start[0], start[1]
    if w == "U":
        target = (x, y+1)
    elif w == "D":
        target = (x, y-1)
    elif w == "L":
        target = (x-1, y)            
    else:
        target = (x+1, y)
    
    if (-5 <= target[0] <=5) and (-5 <= target[1] <= 5):
        return target
    else:
        return start
    