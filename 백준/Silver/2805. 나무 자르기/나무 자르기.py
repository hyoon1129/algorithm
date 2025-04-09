import sys
input = sys.stdin.readline
n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 0, max(tree)
answer = 0
while start <= end:
    mid = (start+end) // 2

    total = 0
    for i in range(n):
        total += max(tree[i] - mid, 0)
    if total >= m:
        answer = mid
        start = mid + 1
    elif total < m:
        end = mid - 1

print(answer)