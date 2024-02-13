def solution(n, results):
    answer = []
    win = {}
    lose = {}
    
    for i in range(n):
        win[i+1] = []
        lose[i+1] = []
    for result in results:
        win[result[0]].append(result[1])
            
        lose[result[1]].append(result[0])
        
    for i in range(1,n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer.append(i)
    
    for i in range(n):
        for num in win:
            for k in win[num]:
                win[num] = list(set(win[num]+win[k]))
    
    # print(win)
    # print(answer)
    for i in range(n):
        cnt = 0
        for num in win:
            if len(win[num]) == i:
                cnt += 1
                node = num
        if cnt == 1:
            answer.append(node)
        else:
            break
    
    for i in win:
        if len(win[i]) == n-1:
            answer.append(i)
        
    return len(set(answer))