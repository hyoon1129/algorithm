# A : 300초
# B : 60초
# C : 10초


t = int(input())

if t%10 != 0:
    print(-1)
    exit()

a, b, c = 0, 0, 0
remain = t

a = remain // 300
remain -= a*300
b = remain // 60
remain -= b*60
c = remain // 10
remain -= c*10

if remain != 0:
    print(-1)
    exit()
    
print(a, b, c)