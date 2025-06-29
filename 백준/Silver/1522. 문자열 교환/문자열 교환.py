s = input()

a = s.count('a')
ss = s + s
cnt = 10**9

for i in range(len(s)):
    window = ss[i:i+a]
    cnt = min(cnt, window.count('b'))

print(cnt)