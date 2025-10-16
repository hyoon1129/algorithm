import math

def solution(n,a,b):
    answer = 1
    
    while True:
        if a == b:
            return answer-1
        else:
            answer += 1
        a = math.ceil(a/2)
        b = math.ceil(b/2)

    return answer