import math
def solution(progresses, speeds):
    answer = []
    days = []
    
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
        
    stack = []
    stack.append(days[0])
    for k in range(1, len(days)):
        if stack[0]>=days[k]:
            stack.append(days[k])
        else:
            answer.append(len(stack))
            stack = [days[k]]
    answer.append(len(stack))
    return answer