# 3의 배수 AND 5의 배수 : FizzBuzz
# 3의 배수 NOT 5의 배수 : Fizz
# NOT 3의 배수 5의 배수 : Buzz
# else: i

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0 and n % 5 != 0:
        print("Fizz")
    elif n % 3 != 0 and n % 5 == 0:
        print("Buzz")
    else:
        print(int(n))
    return


li = []
idx = 0

for i in range(3):
    s = input()
    if s.isdigit():
        idx = i
        num = int(s)
        break

fizzbuzz(num+(3-idx))