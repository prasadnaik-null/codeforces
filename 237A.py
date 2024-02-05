# 237A - Free Cash
d = {}
for i in range(int(input())):
    z = tuple(map(int, input().split()))
    try:
        d[z] += 1
    except:
        d[z] = 1
print(max(map(int, d.values())))