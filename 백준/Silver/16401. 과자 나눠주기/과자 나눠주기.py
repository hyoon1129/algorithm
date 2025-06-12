m, n = map(int, input().split())
li = list(map(int, input().split()))


start = 1
end = max(li)
result = 0
while start <= end:
    cnt = 0
    mid = (start+end) // 2
    
    for snack in li:
        cnt += snack//mid

    if cnt >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)