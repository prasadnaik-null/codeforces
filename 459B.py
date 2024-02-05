# 459B - Pashmak and Flowers
n, l = int(input()), list(map(int, input().split()))
m,M=min(l),max(l)
if m!=M:
    print(max(l)-min(l), l.count(min(l))*l.count(max(l)))
else:
    print(0,((n-1)*n)//2)