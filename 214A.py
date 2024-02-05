# 214A - System of Equations
[m, n], a = sorted(list(map(int, input().split()))), 0
for i in range(int(m**(1./2))+1):
    if n == i+(m-i**2)**2:
        a += 1
print(a)