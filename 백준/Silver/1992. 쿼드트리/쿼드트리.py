n = int(input())


matrix = []

for i in range(n):
    matrix.append(list(map(int, input())))

def compress(x, y, size):
    first = matrix[x][y]
    is_same = True
    for i in range(x, x+size):
        for j in range(y, y+size):
            if matrix[i][j] != first:
                is_same = False
                break
        if not is_same:
            break

    if is_same:
        return str(first)

    half = size//2

    a = compress(x, y, half)
    b = compress(x, y+half, half)
    c = compress(x+half, y, half)
    d = compress(x+half, y+half, half)

    return f"({a}{b}{c}{d})"


print(compress(0,0,n))