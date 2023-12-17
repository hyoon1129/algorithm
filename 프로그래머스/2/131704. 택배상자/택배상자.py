def solution(order):
    answer = 0
    cnt = 0
    bojo = []
    i = 1
    while i < len(order)+1:
        bojo.append(i)
        while bojo and bojo[-1] == order[cnt]:
            cnt += 1
            bojo.pop()
        i += 1
    
    return cnt