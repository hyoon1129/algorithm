import sys
input = sys.stdin.readline

writing = input().strip()
word = input().strip()

wlen = len(word)-1
answer = 0
idx = 0

while len(writing) >= len(word) :
    if word in writing:
        answer += 1
        writing = writing.replace(word, '0', 1)
    else:
        break
print(answer)