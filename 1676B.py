# 1676B - Equal Candies
for _ in range(int(input())):
    n,l=int(input()),list(map(int, input().split()))
    m=min(l)
    s=0
    for i in l:
        s+=(i-m)
    print(s)