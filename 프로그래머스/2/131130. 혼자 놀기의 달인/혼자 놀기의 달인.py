def solution(cards):
    answer = []
    visited = [False for i in range(len(cards)+1)]
    
    
    for i in range(len(cards)):
        tmp = []
        if visited[cards[i]] is False:
            while cards[i] not in tmp:
                tmp.append(cards[i])
                visited[cards[i]] = True
                i = cards[i] - 1
            answer.append(len(tmp))
        
    answer.sort(reverse = True)
    if answer[0] == len(cards):
        return 0
    return answer[0] * answer[1]