import heapq

def solution(jobs):
    answer = 0
    
    jobs.sort()
    
    start = -1 # 바로 전 작업의 시작 시간
    now = 0 # 현재 시간
    cnt = 0 # 처리된 작업의 개수
    
    hq = []
        
    while cnt < len(jobs):
        for i in jobs: # 현재 처리할 수 있는 작업들을 hq에 넣어줌
            if start < i[0] <= now:
                heapq.heappush(hq, [i[1], i[0]]) # 소요 시간 기준으로 정렬되게
        
        if len(hq)>0: # 처리할 작업이 남은 경우
            current = heapq.heappop(hq)
            start = now
            now += current[0]
            answer += now-current[1]
            cnt += 1
        else: # 처리할 작업이 없으면
            now += 1
            
        
    
    
#     jobs.sort(key = lambda x : -x[0])
#     dic = {}
    
    
#     hq = []
#     heapq.heapify(hq)
#     for job in jobs:
#         heapq.heappush(hq, job[1])
#         dic[job[1]] = job[0]
        
#     dis = 0
#     now =0
#     for i in range(len(hq)):
#         p = heapq.heappop(hq)
#         now = (max(dic[p], now)+p)
#         print(p,now)
#         answer += (now-dic[p])


        
    return answer//len(jobs)