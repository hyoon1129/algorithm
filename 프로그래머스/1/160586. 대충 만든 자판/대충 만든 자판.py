def solution(keymap, targets):
    answer = []
    
    dic = {}
    for k in keymap:
        for i in range(len(k)):
            if k[i] in dic:
                if i+1 < dic[k[i]]:
                    dic[k[i]] = i+1
            else:
                dic[k[i]] = i+1

    for target in targets:
        temp = 0
        for i in range(len(target)):
            if target[i] in dic:
                temp += dic[target[i]]
            else:
                temp = -1
                break
        answer.append(temp)
        
    return answer