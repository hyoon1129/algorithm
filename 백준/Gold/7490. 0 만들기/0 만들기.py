from itertools import product

t = int(input())

def solution(n):
    li = []
    for p in product([' ', '+', '-'], repeat=n-1):
        li.append(''.join(p))

    expression = []

    for i in range(len(li)):
        s = ''
        operator = li[i]
        for j in range(1, n+1):
            if j != n:
                s += str(j)+operator[j-1]
            else:
                s += str(j)
        expression.append(s)

    answer = []

    for e in expression:
        ee = e.replace(" ", "")
        if eval(ee) == 0:
            answer.append(e)

    return answer

for i in range(t):
    n = int(input())
    result = solution(n)

    for j in range(len(result)):
        print(result[j])
    if i != t-1:
        print()