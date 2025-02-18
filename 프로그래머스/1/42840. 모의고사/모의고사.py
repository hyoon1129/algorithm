def solution(answers):
    answer = []
    ans1 = [1,2,3,4,5]
    ans2 = [2,1,2,3,2,4,2,5]
    ans3 = [3,3,1,1,2,2,4,4,5,5]
    
    cnt = [0,0,0]
    
    i = 0
    
    for i in range(len(answers)):
        if ans1[i%5] == answers[i] :
            cnt[0] += 1
        if ans2[i%8] == answers[i] :
            cnt[1] += 1
        if ans3[i%10] == answers[i] :
            cnt[2] += 1
            
    for k in range(3):
        if cnt[k] == max(cnt) :
            answer.append(k+1)
    return answer