m, n = map(int, input().split())

def get_primes(num):
    is_prime = [True] * (num + 1)
    is_prime[0] = is_prime[1] = False
    
    
    for i in range(2, int(num**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, num+1, i):
                is_prime[j] = False
    return is_prime

is_prime = get_primes(n)

for i in range(m, n+1):
    if is_prime[i]:
        print(i)