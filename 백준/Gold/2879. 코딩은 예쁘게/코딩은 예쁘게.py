import sys
input = sys.stdin.readline

n = int(input())
now = list(map(int, input().split())) # 현재 줄의 탭의 개수
target = list(map(int, input().split())) # 올바른 탭의 개수

move = [] # 올바른 탭으로 가기 위해 필요한 탭 수
for i in range(n):
    move.append(target[i] - now[i])

answer = 0


def get_edit(group):
    global answer

    if group == [] or (min(group) == 0 and max(group)== 0):
        return

    minimum = min(group)
    midx = group.index(minimum)
    answer += group[midx]

    for i in range(len(group)):
        group[i] = group[i] - minimum

    get_edit(group[:midx])
    get_edit(group[midx+1:])



group = []
group.append(abs(move[0]))

for i in range(0, n-1):
    if move[i] * move[i+1] <= 0:
        get_edit(group)
        group = []
    group.append(abs(move[i+1]))

get_edit(group)

print(answer)

'''
 처음에는 +이냐 -이냐에 따라서 그룹을 나누고 그 그룹에서 abs max 값을 더하는 방식으로 했는데,
 그렇게 하면 
 5
 3 2 1 2 3
 0 0 0 0 0
 이 입력으로 들어왔을 때 답을 3으로 출력한다. (답은 5)
 3 2 1 2 3 -> 2 1 0 1 2 가 된다!!
 그래서 다시 그룹은 2 1 / 1 2 로 나누고 나누고 나누고 .. 이런 식으로 재귀로 풀었다
'''
