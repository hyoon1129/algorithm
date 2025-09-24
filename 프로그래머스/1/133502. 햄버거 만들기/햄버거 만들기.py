def solution(ingredient):
    # 1, 2, 3, 1
    answer = 0
    
    i = 0
    while i <= len(ingredient) - 4:
        if ingredient[i:i+4] == [1, 2, 3, 1]:
            del ingredient[i:i+4]
            answer += 1
            i = max(0, i-3)
        else:
            i += 1
            
    return answer























# def solution(ingredient):
#     answer = 0
#     i = 0
#     while i <= len(ingredient) - 4 :
#         if ingredient[i:i+4] == [1,2,3,1]:
#             answer += 1
#             del ingredient[i:i+4]
#             i = max(0,i-2)
#         else:
#             i += 1
    
#     return answer