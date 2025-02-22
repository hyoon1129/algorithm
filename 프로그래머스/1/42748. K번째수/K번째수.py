def solution(array, commands):
    answer = []
    for command in commands:
        slicing = sorted(array[command[0]-1:command[1]])
        answer.append(slicing[command[2]-1])
    return answer