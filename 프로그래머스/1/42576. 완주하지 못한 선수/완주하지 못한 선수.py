def solution(participant, completion):
    dic = {}
    
    for name in completion:
        if name in dic:
            dic[name] += 1
        else:
            dic[name] = 1
    
    for c in participant:
        if c in dic:
            if dic[c] > 1:
                dic[c] -= 1
            else:
                del dic[c]
        else:
            return c
            












# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for i in range(len(participant)-1) :
#         if participant[i] != completion[i]:
#             return participant[i]
#     return participant[-1]