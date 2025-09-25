def solution(brown, yellow):
    
    # 넓이 = brown + yellow
    area = brown + yellow
    
    for i in range(1, area+1):
        if area % i == 0:
            if (i-1)*2 + ((area//i)-1) * 2 == brown:
                answer = [((area//i)), i]
                break
    return answer