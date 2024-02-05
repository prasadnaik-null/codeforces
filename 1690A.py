# 1690A - Print a Pedestal (Codeforces logo?)
for _ in range(int(input())):
    n = int(input())-6
    q = n//3
    r = n % 3
    print(2+(q+(r+1)//3), 3+(q+(r+2)//3), 1+q)