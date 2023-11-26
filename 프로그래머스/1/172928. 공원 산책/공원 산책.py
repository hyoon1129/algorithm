def solution(park, routes):
    global start, x, limit
    answer = []
    x = []
    limit = [len(park), len(park[0])]
    start = []
    
    
    for i in range(limit[0]):
        for j in range(limit[1]):
            if park[i][j] == 'S':
                start = [i,j]
            elif park[i][j] == 'X':
                x.append([i,j])
    
    for route in routes:
        start = check(route, x)
    
    return start
    
    
            
def check(route, x):
    move = []
    
    # 장애물을 만나는지 검사
    if route[0] == 'E':
        move = [start[0], start[1]+int(route[-1])]
        for i in range(start[1], move[1]+1):
            if [start[0], i] in x:
                return start
                
            
    elif route[0] == 'W':
        move = [start[0], start[1]-int(route[-1])]
        for i in range(move[1], start[1]+1):
            if [start[0], i] in x:
                return start
            
    elif route[0] == 'S':
        move = [start[0]+int(route[-1]), start[1]]
        for i in range(start[0], move[0]+1):
            if [i, start[1]] in x:
                return start
            
    else:
        move = [start[0]-int(route[-1]), start[1]]
        for i in range(move[0], start[0]+1):
            if [i, start[1]] in x:
                return start
    
    
    # 공원 밖을 벗어나는지 검사
    if move[0] >= limit[0] or move[1] >= limit[1]:
        return start
    if move[0] < 0 or move[1] < 0:
        return start
    
    return move






'''
def solution(park, routes):
    answer = []
    x = []
    limit = [len(park)-1, len(park[0])-1]
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                start = [i,j]
            elif park[i][j] == 'X':
                x.append([i,j])
    
    for route in routes:
        start = move(limit, start, int(route[2]), x, route[0]) 
            
    return start

def move(limit, start, distance, x, where):
    if where == 'S':
        if start[0]+distance > limit[0]:
            return start
        for i in range(1,distance+1):
            if ([start[0]+i, start[1]] in x):
                return start
        return [start[0]+distance, start[1]]
    
    elif where == 'N':
        if start[0]-distance < 0:
            return start
        for i in range(1,distance+1):
            if ([start[0]-i, start[1]] in x):
                return start
        return [start[0]-distance, start[1]] 
    
    elif where == 'E':
        if start[1]+distance > limit[1]:
            return start
        for i in range(1,distance+1):
            if ([start[0], start[1]+i] in x):
                return start
        return [start[0], start[1]+distance]
    
    else:
        if start[1]-distance < 0:
            return start
        for i in range(1,distance+1):
            if ([start[0], start[1]-i] in x):
                return start
        return [start[0], start[1]-distance]
        '''