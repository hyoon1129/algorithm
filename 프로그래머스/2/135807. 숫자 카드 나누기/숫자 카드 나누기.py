import math

def solution(arrayA, arrayB):
    answer = 0
    gcdA = 0
    gcdB = 0
    a = arrayA[0]
    b = arrayB[0]
    
    
    
    if len(arrayA) == 1:
        gcdA = a
    else:
        for i in range(1, len(arrayA)):
            gcdA = math.gcd(a, arrayA[i])
            a = gcdA
    
    if len(arrayB) == 1:
        gcdB = b
    else:
        for j in range(1, len(arrayB)):
            gcdB = math.gcd(b, arrayB[j])
            b = gcdB
        
        
    
    check_a = 1
    check_b = 1
    for i in range(len(arrayA)):
        if arrayA[i] >= gcdB and (gcdB == 0 or arrayA[i] % gcdB == 0):
            gcdB = 0
            break

    for i in range(len(arrayB)):
        if arrayB[i] >= gcdA and (gcdA == 0 or arrayB[i] % gcdA == 0):
            gcdA = 0
            break
    
    return max(gcdA, gcdB)
        


'''
def solution(arrayA, arrayB):
    answer = []
    
    arrayA.sort(reverse = True)
    arrayB.sort(reverse = True)
    
    if (len(arrayA) == 1) and (len(arrayB)) == 1:
        answer = [max(arrayA[0], arrayB[0])]
        
    else:
        print(check(arrayA, newGCD(arrayB)), check(arrayB, newGCD(arrayA)))
        answer.append(check(arrayA, newGCD(arrayB)))
        answer.append(check(arrayB, newGCD(arrayA)))
        
        
    
    
    return max(answer)

def check(arr, g):
    if g == 0:
        return 0
    
    for i in arr:
        if i%g == 0:
            return 0
        
    return g
    

def newGCD(arr):
    result = 0
    copy = []
    copy = arr.copy()
    
    if len(copy) == 2 :
        return math.gcd(copy[0], copy[1])
    
    for i in range(len(arr)-1):
        result = math.gcd(copy[i], copy[i+1])
        copy[i+1] = result
        
    return result
'''

        