def solution(s):
    answer = True
    
    stack = ""
    
    for i in range(len(s)):
        stack += s[i]
        if stack[-2:] == "()":
            stack = stack[:-2]
    if stack == "":
        return True
    return False










# def solution(s):
#     answer = True
#     li = []
#     for i in range(len(s)):
#         li.append(s[i])
#         if len(li)>=2:
#             if li[-2]=='(' and li[-1] == ')':
#                 li.pop()
#                 li.pop()
#     if len(li)==0:
#         return True
#     return False