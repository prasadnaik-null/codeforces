# 1474B - Different Divisors
def isP(n):
    prime_flag = 0
    for i in range(2, int(n**0.5) + 1):
        if (n % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        return True
    else:
        return False


for _ in range(int(input())):
    n = int(input())
    i = n+1
    while not isP(i):
        i += 1
    x = i+n
    while not isP(x):
        x += 1
    print(i*x)