def solution(wallpaper):
    width = []
    length = []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                width.append(i)
                length.append(j)
    
    return [min(width), min(length), max(width)+1, max(length)+1]