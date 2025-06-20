from collections import deque
n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([False] * n)

step = 0

while True:
    step += 1

    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = False # 내려가는 위치 로봇 내리기

    for i in range(n-2, -1, -1):
        if robot[i] and not robot[i+1] and belt[i+1] > 0:
            robot[i] = False
            robot[i+1] = True
            belt[i+1] -= 1
    robot[-1] = False

    if belt[0] > 0:
        robot[0] = True
        belt[0] -= 1
    if belt.count(0) >= k:
        break

print(step)