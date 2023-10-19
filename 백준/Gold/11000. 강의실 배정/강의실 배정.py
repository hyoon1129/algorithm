import sys
input = sys.stdin.readline
import heapq

n = int(input())
li = []
answer = 0

for i in range(n):
    li.append(list(map(int, input().split())))

li.sort()
room = []
heapq.heappush(room, li[0][1]) # 젤 먼저 시작하는 강의의 끝나는 시간 저장

for i in range(1, n):
    if li[i][0] < room[0]: # 같은 강의실에서 할 수 없으면
        heapq.heappush(room,li[i][1]) # 새 강의실 개설

    else: # 같은 강의실에서 할 수 있으면
        heapq.heappop(room) # 새로운 수업으로 시간 변경. pop하고 새 시간 push
        heapq.heappush(room, li[i][1])

print(len(room))
