def solution(name):
    answer = 0
    #A B C D E F G H I J 
    
    for s in name:
        result = ord(s) - ord('A')
        answer += min(result, 26-result)
    
    
    
    print(answer)
#     right = 0
#     left = 0
#     for i in range(1, len(name)):
#         if name[i] != "A":
#             break
#         else:
#             right += 1
            
#     for i in range(len(name)-1, 0, -1):
#         if name[i] != "A":
#             break
#         else:
#             left += 1
    
#     answer += (len(name)-max(right, left)-1)

# 1. 오른쪽으로 쭉 가거나, 2. 왼쪽으로 쭉 가거나, 3. 오른쪽 가다가 왼쪽으로, 4. 왼쪽 가다가 오른쪽으로

    lenA = 0
    astart= 0
    aend = 0
    for i in range(1, len(name)+1):
        if 'A'*i in name:
            lenA = i
            astart = name.find('A'*i)
            aend = astart + i - 1
        else:
            break
    print(astart, aend)
    #   
    shift = len(name)-1
    # shift = min(len(name) - lenA + min(astart-2, len(name)-aend-1), shift)
    while name[shift] == 'A' and shift > 0:
        shift -= 1
        
    if astart == 0 and aend == 0:
        answer += shift
    elif astart == 0 and aend != 0:
        answer += min(shift, len(name)-aend-1)
    else:
        shift = min((len(name)-aend-1)*2+astart-1,(astart-1)*2 + len(name) - aend - 1, shift)
        answer += shift
    return answer