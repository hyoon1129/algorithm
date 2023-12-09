# from itertools import product

# def solution(n):
#     answer = ''
#     num = ["1","2","4"]
#     li = []
#     nara = []
#     for i in range(300):
#         pro = list(map(''.join, product(num, repeat = i+1)))
#         a = ''
#         for j in pro:
#             nara.append(j)
            
#     return nara[n-1]

def solution(n):
    answer = ''
    
    while n > 0:
        if n%3 != 0:
            answer += str(n%3)
            n = n//3
        else:
            answer += '4'
            n = n//3 - 1
    return answer[::-1]