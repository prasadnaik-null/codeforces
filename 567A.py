# 567A - Lineland Mail
n, x = int(input()), sorted(list(map(int, input().split())))
x = [x[1]]+x+[x[n-2]]
for i in range(1, 1+n):
    print(min(abs(x[i]-x[i-1]), abs(x[i+1]-x[i])),
          max(abs(x[i]-x[1]), abs(x[n]-x[i])))