import sys
input = sys.stdin.readline

writing = input().strip()
word = input().strip()

wlen = len(word)

answer = 0
idx = 0
while idx < len(writing):
    if writing[idx:idx+wlen] == word:
        answer += 1
        idx += wlen
    else:
        idx += 1
print(answer)