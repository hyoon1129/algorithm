import math
a, b = map(int, input().split())
c, d = map(int, input().split())

bunmo = b*d
bunja = a*d + c*b

gcd = math.gcd(bunmo, bunja)

print(bunja//gcd, bunmo//gcd)