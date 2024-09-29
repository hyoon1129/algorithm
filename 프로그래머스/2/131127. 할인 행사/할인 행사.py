def solution(want, number, discount):
    dic = {}
    li = []
    answer = 0
    for i in range(len(want)):
        dic[want[i]] = number[i]
        for j in range(number[i]):
            li.append(want[i])

    li.sort()
    # if len(set(discount)) < len(number):
    #     return 0

    
    for i in range(len(discount)-10+1):
        if sorted(discount[i:i+10]) == li:
            answer += 1
    return answer
    
    
    





# import collections
# def solution(want, number, discount):
#     answer = 0
#     dic = {}
#     for a, b in zip(want, number):
#         dic[a] = b
    
#     for i in range(len(discount)-9):
#         if collections.Counter(discount[i:i+10]) == dic:
#             answer += 1
#     return answer