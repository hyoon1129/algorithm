from collections import deque
t = int(input())

def solution():
    n, m = map(int, input().split())
    paper = deque(map(int, input().split()))

    value = paper[m]
    paper[m] = -1


    cnt = 0
    while True:
        current_max = max([x if x != -1 else value for x in paper])
        front = paper[0] if paper[0] != -1 else value
        if current_max > front:
            paper.append(paper[0])
            paper.popleft()
        else:
            cnt += 1
            if paper[0] == -1:
                print(cnt)
                break
            paper.popleft()

    return

for i in range(t):
    solution()