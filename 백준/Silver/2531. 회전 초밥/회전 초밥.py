n, d, k, c = map(int, input().split())
# 접시 수, 초밥 가짓수, 연속 접시 수, 쿠폰 번호

sushi = [int(input()) for _ in range(n)]
sushi += sushi[:k-1]

answer = 0
for i in range(n):
    if c not in sushi[i:i+k]:
        answer = max(answer, len(set(sushi[i:i+k]))+1)
    else:
        answer = max(answer, len(set(sushi[i:i+k])))
print(answer)