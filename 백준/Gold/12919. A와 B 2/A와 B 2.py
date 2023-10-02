import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

s = input().strip()
t = input().strip()
answer = 0
def solution(s, t):
    global answer
    if (s not in t) and (s[::-1] not in t):
        return

    if len(s) == len(t):
        if s == t:
            answer = 1
        return
    solution(s+"A", t)
    solution((s+"B")[::-1],t)

solution(s,t)
print(answer)