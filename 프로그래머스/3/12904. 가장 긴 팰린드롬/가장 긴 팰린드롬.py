def solution(s):
    answer = 0

    reverse = s[::-1]
    
    for i in range(len(s)):
        for j in range(i+1):
            if s[j:j+len(s)-i] == reverse[len(s)-(j+len(s)-i):len(s)-j]:
                return len(s)-i
            
        
    return answer