t = int(input())


def solution(s, k):
    dic = {}
    for i in range(len(s)):
        if s[i] in dic:
            dic[s[i]].append(i)
        else:
            dic[s[i]] = [i]

    ans3 = 10**9
    ans4 = -10**9
    for indexes in dic.values():
        if len(indexes) < k:
            continue
        for i in range(len(indexes)-k+1):
            length = indexes[i+k-1]-indexes[i] + 1
            ans3 = min(ans3, length)
            ans4 = max(ans4, length)

    if ans3 == 10**9 or ans4 == -10**9:
        print(-1)
    else:
        print(ans3, ans4)
    return

for _ in range(t):
    s = input()
    k = int(input())
    solution(s, k)