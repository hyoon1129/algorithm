def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        temp = i
        num = i
        while True:
            if temp == n:
                answer += 1
                break
            elif temp > n:
                break
            num += 1
            temp += num
            
                
            
    return answer
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# def solution(n):
#     answer = 0
    
#     for i in range(1,n+1):
#         temp = i
#         while True:
#             if i == n:
#                 answer += 1
#                 break
#             elif i > n:
#                 break
#             temp += 1
#             i += temp
#     return answer