n = int(input())
a = list(map(int, input().split()))  # i번째 날에 받아야 하는 최소 금액
b = list(map(int, input().split()))  # j번째 자루에 담은 금액

if sum(a) > sum(b):
    print(-1)
    exit()

# 자루를 정렬
b.sort()

# 요구사항을 (금액, 원래 인덱스)로 만들어 금액 기준 내림차순 정렬
events = sorted([(a[i], i) for i in range(n)], reverse=True)

used = [False] * n
answer = [0] * n
last_used = -1  # 마지막으로 사용한 인덱스

# 각 요구사항에 대해 조건을 만족하는 가장 작은 자루 할당
for amount, day in events:
    # 이진 탐색으로 시작점 찾기
    left, right = 0, n - 1
    start = n
    
    while left <= right:
        mid = (left + right) // 2
        if b[mid] >= amount:
            start = mid
            right = mid - 1
        else:
            left = mid + 1
    
    # start부터 시작해서 사용하지 않은 첫 번째 자루 찾기
    found = False
    for i in range(max(start, last_used + 1), n):
        if not used[i]:
            answer[day] = b[i]
            used[i] = True
            last_used = i
            found = True
            break
    
    # 앞쪽에서 다시 찾기
    if not found:
        for i in range(start, min(last_used + 1, n)):
            if not used[i]:
                answer[day] = b[i]
                used[i] = True
                found = True
                break
    
    if not found:
        print(-1)
        exit()

print(*answer)