def solution(s):
    s = s.split(" ")
    
    li = []
    
    for num in s:
        li.append(int(num))
        
    return str(min(li)) + " " + str(max(li))















# def solution(s):
#     answer = ''
    
#     arr = s.split()
#     int_arr = []
#     for i in arr:
#         int_arr.append(int(i))

#     answer = str(min(int_arr)) + ' ' + str(max(int_arr))
#     return answer