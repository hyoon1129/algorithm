def solution(arr):
    
    answer = 0
    arr.sort(reverse = True)
    
    if sum(arr) == 0:
        return 0
    
    for i in range(len(arr)):
        if i < arr[i]:
            answer = i
        else:
            break
    return answer + 1