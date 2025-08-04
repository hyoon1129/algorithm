n, k = map(int, input().split())

a = list(map(int, input().split()))

dic = {}
left = 0
answer = 0

for right in range(n):
    dic[a[right]] = dic.get(a[right], 0) + 1

    while dic[a[right]] > k:
        dic[a[left]] -= 1
        left += 1
    answer = max(answer, right-left+1)
print(answer)