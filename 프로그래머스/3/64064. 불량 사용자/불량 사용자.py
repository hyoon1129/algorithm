from itertools import combinations, permutations

def solution(user_id, banned_id):
    answer = []
    for perm in permutations(user_id, len(banned_id)):
        
        
        if check_len(perm, banned_id) is False:
            continue
        
        
        for i in range(len(perm)):
            eql = True
            if check_equal(perm[i], banned_id[i]) is False:
                eql = False
                break
                
        if eql is True:
            li = sorted(list(perm))
            if li not in answer:
                answer.append(li)
            
    return len(answer)
            
            
                
def check_len(li1, li2):
    for i in range(len(li1)):
        if len(li1[i]) != len(li2[i]):
            return False
    return True

def check_equal(id1, id2):
    for i in range(len(id1)):
        if id1[i] != id2[i] and id2[i] != '*':
            return False
    return True
        