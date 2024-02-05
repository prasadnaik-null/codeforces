# 478B - Random Teams
def add(x):
    return (x*(x-1))//2


[n, m] = list(map(int, input().split()))
kmax = add(n-m+1)
q, r = n//m, n % m
kmin = r*add(q+1)+(m-r)*add(q)
print(kmin, kmax)