# 1343C - Alternating Subsequence
def sign(x):
    if x > 0:
        return "+"
    else:
        return "-"


for _ in range(int(input())):
    n, l = int(input()), list(map(int, input().split()))
    k = sign(l[0])
    m = l[0]
    s = 0
    for i in l:
        if k == sign(i):
            if m < i:
                m = i
        else:
            s += m
            m = i
            k = sign(i)
    print(s+m)