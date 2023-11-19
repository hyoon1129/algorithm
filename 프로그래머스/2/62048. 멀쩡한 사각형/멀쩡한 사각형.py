import math

def solution(w,h):
    answer = 1
    a = float(h) / float(w)
    
    if w == h:
        return w*h - w
    
    if w == 1 or h == 1:
        return 0
    
    answer = w*h
    
    for i in range(1, w+1):
        answer -= math.ceil((float(h)*i) / float(w))-(math.floor((float(h)*(i-1)/float(w))))
    
    return answer