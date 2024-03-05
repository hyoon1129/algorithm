def solution(msg):
    answer = [0]
    dic = {}
    
    # 사전 초기화
    for i in range(ord("A"), ord("Z")+1):
        dic[chr(i)] = i-ord("A")+1
        
    dnum = 27
    
    base = ""
    
    for i in range(len(msg)):
        base += msg[i]
        
        if base not in dic:
            dic[base] = dnum
            dnum += 1
            base = msg[i]
            answer.append(dic[base])
        else:
            answer[-1] = dic[base]
    
    return answer
        
    
    
#     while index <= len(msg)-2:
#         if index == len(msg)-2:
#             answer.append(dic[msg[index+1]])
#             break
#         if w in dic and w+c not in dic:
#             answer.append(dic[w])
#             dic[w+c] = dnum
#             dnum += 1
#             index += 1
            
#             w = msg[index]
#             c = msg[index+1]
#         elif w+c in dic:
#             w = w + c
#             c = msg[index+1]
#     print(dic)
        
    
    
    return answer