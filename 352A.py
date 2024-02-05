# 352A - Jeff and Digits
n, l = int(input()), list(map(int, input().split()))
if l.count(0)>0:
    print(int("5"*((l.count(5)//9)*9)+"0"*(l.count(0))))
else:
    print(-1)