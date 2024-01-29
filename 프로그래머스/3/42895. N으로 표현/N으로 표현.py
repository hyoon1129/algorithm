def solution(N, number):
    answer = 0
    
    
    if N == number:
        return 1
    print(set(list(str(number))))
    
    if set(list(str(number))) == {str(N)}:
        return len(str(number))
    
    # if number % N == 0:
    #     if N != 1:
    #         return len(str(number))
        
    # elif N != 1 and number%N == 0:
    #     return len(str(number))
    
    dp = [[] for i in range(9)]
    
    dp[1] = [N]
    dp[2] = [int(str(N)*2), N*N, N+N, N-N, N//N]
    
    for i in range(3, 9):
        result = []
        
        for j in range(1, i):
            result = result + operations(dp[j], dp[i-j]) + operations(dp[i-j], dp[j])
            
        result.append(int(str(N)*i))
        result = list(set(result))
        dp[i] = result
        
        if number in dp[i]:
            return i
    
    return -1


def operations(a, b):
    result = []
    for i in a:
        for j in b:
            result.append(i+j)
            result.append(i*j)
            if i>=j:
                result.append(i-j)
            if j != 0: 
                result.append(i//j)
    return result
            