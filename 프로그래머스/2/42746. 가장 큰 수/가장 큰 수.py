def solution(numbers):
    answer = ''
    
    s_num = []
    
    for i in range(len(numbers)):
        s_num.append(str(numbers[i]))

    s_num = sorted(s_num, key = lambda x:x*4, reverse = True)

    for num in s_num:
        answer += str(int(num))
    
    return str(int(answer))