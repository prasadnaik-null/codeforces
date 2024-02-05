# 489C - Given Length and Sum of Digits...
[m, s] = list(map(int, input().split()))
if s == 0:
    if m == 1:
        print(0, 0)
    else:
        print(-1, -1)
elif s > 9*m:
    print(-1, -1)
else:
    q1, q2, r1, r2 = s//9, (s-1)//9, s % 9, (s-1) % 9
    m1 = str(int("1"+"0"*(m-1))+int(str(r2)+"9"*q2))
    m2 = ("9"*q1+str(r1)+"0"*(m-q1-1))
    print(m1[:m], m2[:m])