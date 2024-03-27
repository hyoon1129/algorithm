import copy
import sys

global N, L
N, L = map(int, input().split())

roads = []
answer = 0

for i in range(N):
    roads.append(list(map(int, input().split())))


for i in range(N):
    column = []
    for j in range(N):
        column.append(roads[j][i])
    roads.append(column)


def check_route(road):
    visited = [0] * N
    for i in range(N-1):
        if road[i] == road[i+1]:
            continue
        elif abs(road[i]-road[i+1]) > 1: # 높이 차이 2 이상이면 경사로 x
            return False

        elif road[i] < road[i+1]: # 오르막길
            if i-L < -1:
                return False
            check = road[i]
            for j in range(i, i-L, -1):
                if visited[j] or road[j]!=check:
                    return False
                visited[j] = 1
        else: # 내리막길
            if i+L >= N :
                return False
            check = road[i+1]
            for j in range(i+1, i+L+1):
                if visited[j] or road[j]!=check:
                    return False
                visited[j] = 1
    return True


for road in roads:
    if check_route(road):
        answer += 1

print(answer)