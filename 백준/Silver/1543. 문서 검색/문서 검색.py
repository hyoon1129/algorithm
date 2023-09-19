import sys
input = sys.stdin.readline

writing = input()
word = input().strip()

answer = 0

while len(writing) >= len(word) :
    if word in writing:
        answer += 1
        writing = writing.replace(word, '0', 1)
    else:
        break
print(answer)


# word를 input 받을 때 개행문자까지 포함되었다. strip으로 제거해주기
