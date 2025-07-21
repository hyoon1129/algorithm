a, d, k = map(int, input().split())

if d == 0:
    print(1 if a == k else 'X')
elif (k-a) % d != 0 or (k-a) // d < 0:
    print('X')
else:
    print((k-a)//d + 1)