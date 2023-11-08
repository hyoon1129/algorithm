import sys
input = sys.stdin.readline

n = int(input())
have = list(map(int, input().split()))
m = int(input())
card = list(map(int, input().split()))
have.sort()

def binary_search(target, start, end):
    global have

    while start+1 < end:
        mid = (start + end) // 2

        if have[mid] == target:
            return 1

        elif have[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    if target in [have[start], have[end]]:
        return 1
    return 0

for i in card:
    print(binary_search(i, 0, len(have)-1), end = ' ')