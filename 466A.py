# 466A - Cheap Travel
[n, m, a, b] = list(map(int, input().split()))
if a*m <= b:
    print(n*a)
else:
    z = (n//m)*b
    print(min(z+b, z+(n % m)*a))