from collections import deque

def bfs(start, new_tickets):
    queue = deque()
    length = len(new_tickets)+1
    queue.append((start,new_tickets))
    
    
    while queue:
        route, now_t = queue.popleft()
        
        if route is None:
            continue
        
        if len(now_t) == 0:
            if route not in answer:
                answer.append(route)
            continue

        for ticket in new_tickets:
            if ticket in now_t:
                if ticket[0] == route[-1]:
                    result = route[:]
                    result.append(ticket[1])
                    t = now_t[:]
                    t.remove(ticket)
                    queue.append((result, t))
        

    return 0
            
        

def solution(tickets):
    global answer
    answer = []
    
    candidate = []
    
    for ticket in tickets:
        if ticket[0] == "ICN":
            candidate.append(ticket)
    
    for i in candidate:
        new_tickets = tickets[:]
        new_tickets.remove(i)
        bfs(i,new_tickets)
        
    answer.sort()
    return answer[0]