import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
lcs = [[0]*(len(b)+1) for i in range(len(a)+1)]

a = ' ' + a
b = ' ' + b
lcs[0][0] = 0
lcs[0][1] = 0
lcs[1][0] = 0

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])


print(lcs[len(a)-1][len(b)-1])

# lcs(i, j) : 문자열 a의 i번째까지, 문지열 b의 j번째까지 비교했을 때 lcs


# a[i] == b[j]일 때
# lcs(i, j) = lcs(i, j) + 1
# a[i] != b[j]일 때
# 기존 주어진 문자열ㄹ로 만들 수 있는 최대 lcs 길이
# lcs(i, j) = max(lcs(i-1, j), lcs(i, j-1))


# aabbb
# aacbb
# lcs(2,2) = 2
# i가 2, j가 3일 때
# lcs(2,3) = lcs(i, j-1)
# i가 3, j가 2일 때
# lcs(3,2) = lcs(i-1, j)

# acb
# aba
# lcs = ab
# lcs(1,1) = 1
# lcs(2,1) = lcs(1,1) = 1
# lcs(1,2) = lcs(1,1) = 1
# lcs(2,2) = lcs(1,1)
# lcs(2,3) = lcs(2,2)
# lcs(3,2) = lcs(2,2) + 1

# acaykp
# capcak
# lcs(1,1) = 0
# lcs(1,2) = 1
# lcs(1,3) = 1 (lcs(1,2))
# lcs(1,n) = 1 (lcs(1,n-1))
# lcs(2,1) = lcs(1,1) + 1 (a[i]==b[j])
# lcs(2,2) = 1
# lcs(2,3) = 1
# lcs(2,4) = lcs(2,3) + 1 (a[i]==b[j])