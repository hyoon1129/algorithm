def solution(numbers, target):
    answer = 0
    
    num = [0]
    
    for i in numbers:
        temp = []
        for j in num:
            temp.append(j+i)
            temp.append(j-i)
        num = temp
    
    return num.count(target)