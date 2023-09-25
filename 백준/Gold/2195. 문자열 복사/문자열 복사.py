import sys
input = sys.stdin.readline


s = input().strip()
p = input().strip()

answer = 0

str = ''
idx = 0
while idx < len(p):

    if (str + p[idx]) in s:
        if idx == len(p) - 1:
            answer += 1
            break
        str += p[idx]
        idx += 1
    else:
        answer += 1
        str = ''

print(answer)