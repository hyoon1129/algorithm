import sys
input = sys.stdin.readline

n = int(input())
request = list(map(int, input().split()))
maximum = int(input())

if sum(request) <= maximum :
    print(max(request))
else:
    start, end = 0, max(request)


    while start <= end :
        mid = (start + end) // 2
        total = 0
        for i in request:
            total += min(mid, i)

        if total <= maximum:
            start = mid + 1
        else:
            end = mid - 1

    print(end)
