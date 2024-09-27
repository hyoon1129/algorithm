def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    
    for line in photo:
        result = 0
        for j in range(len(line)):
            if line[j] in dic:
                result += dic[line[j]]
        answer.append(result)
    return answer
        






















# def solution(name, yearning, photo):
#     answer = []
#     for li in photo:
#         result = 0
#         for nm in li :
#             if nm in name:
#                 result += yearning[name.index(nm)]
#         answer.append(result)
#     return answer