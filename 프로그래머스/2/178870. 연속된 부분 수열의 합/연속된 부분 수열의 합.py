def solution(sequence, k):
    answer = []

    start, end = 0, 0
    current_sum = 0
    min_len = 10**9
    
    while start < len(sequence):
        if current_sum == k:
            if min_len > end - start:
                answer = [start, end-1]
                min_len = end - start
            current_sum -= sequence[start]
            start += 1
        elif current_sum < k:
            if end == len(sequence):
                break
            current_sum += sequence[end]
            end += 1
        else:
            current_sum -= sequence[start]
            start += 1
            
    return answer