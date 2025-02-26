def solution(sizes):
    a = []
    b = []
    for li in sizes:
        a.append(sorted(li)[0])
        b.append(sorted(li)[1])
    return max(a)*max(b)
        