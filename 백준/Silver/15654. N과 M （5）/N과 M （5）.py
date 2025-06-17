from itertools import permutations
n, m = map(int, input().split())

li = list(map(int, input().split()))
li.sort()
pmt = permutations(li, m)
answer = []

for p in pmt:
    result = ""
    for i in p:
        result += str(i)
        result += ' '
    answer.append(result)

for i in range(len(answer)):
    print(answer[i])