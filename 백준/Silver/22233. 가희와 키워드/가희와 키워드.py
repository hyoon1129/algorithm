import sys
input = sys.stdin.readline

n, m = map(int, input().split())

memo = set()

for _ in range(n):
    keyword = input().strip()
    memo.add(keyword)

answer = []
result = len(memo)
for _ in range(m):
    post = list(map(str, input().strip().split(",")))

    for word in post:
        if word in memo:
            result -= 1
            memo.remove(word)
    answer.append(result)


for i in range(len(answer)):
    print(answer[i])