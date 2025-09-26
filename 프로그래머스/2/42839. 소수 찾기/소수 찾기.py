from itertools import permutations
def solution(numbers):
    answer = 0

    p = set()
    
    for i in range(1, len(numbers)+1):
        for num in permutations(numbers, i):
            p.add(int(''.join(num)))

    for num in p:
        if check(num):
            answer += 1
    
    return answer

def check(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True