def solution(number, k):
    answer = ''
    
    stack = []
    cnt = 0
    
    for num in number:
        while stack and stack[-1] < num and cnt < k:
            stack.pop()
            cnt += 1
        stack.append(num)
        
    if cnt < k:
        stack = stack[:-(k-cnt)]

    return ''.join(stack)