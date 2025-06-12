s = input()

is_minus = False
answer = 0
num = ""
for i in range(len(s)):
    if s[i] == "+" or s[i] == "-":
        if is_minus:
            answer -= int(num)
        else:
            answer += int(num)
        num = ""
        if s[i] == "-":
            is_minus = True
    else:
        num += s[i]

if is_minus:
    answer -= int(num)
else:
    answer += int(num)
print(answer)