N = int(input())
M = int(input())
S = input()

OI = 'OI'
P = 'I' + OI * N
answer = 0

i = 0
j = 0
while i < M-1:
    if S[i:i+3] == "IOI":
        i += 2
        j += 1
        if j == N :
            answer += 1
            j -= 1
    else:
        i += 1
        j = 0

print(answer)
