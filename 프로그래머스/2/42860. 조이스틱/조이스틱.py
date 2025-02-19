def solution(name):
    answer = 0
    #A B C D E F G H I J 
    
    for s in name:
        result = ord(s) - ord('A')
        answer += min(result, 26-result)

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
            
            
    shift = len(name)-1
    
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