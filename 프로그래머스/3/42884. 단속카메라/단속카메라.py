def solution(routes):
    routes = sorted(routes,key=lambda x:x[1])
    
    cctv = routes[0][1]
    answer = 1
    
    
    for i in range(len(routes)-1):
        if cctv < routes[i+1][0]:
            answer += 1
            cctv = routes[i+1][1]
    return answer

print(solution([[-2,-1], [1,2],[-3,0]])) #2
print(solution([[0,0],])) #1
print(solution([[0,1], [0,1], [1,2]])) #1
print(solution([[0,1], [2,3], [4,5], [6,7]])) #4
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2