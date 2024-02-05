# 1360C - Similar Pairs
def func(d):
    for i in range(9):
        for j in d[i]:
            for k in d[i+1]:
                if j-k == 1:
                    return True
    return False


def ffunc(d):
    for i in d[9]:
        for j in d[0]:
            if i-j == 1:
                return True
    return False


for _ in range(int(input())):
    n, l = int(input()), list(map(int, input().split()))
    o, e = 0, 0
    d = [[]]*10
    for i in l:
        if i % 2 == 0:
            e += 1
        else:
            o += 1
        d[i % 10].append(i)
    if (e % 2 == 0 and o % 2 == 0) or (e % 2 == 1 and o % 2 == 1 and (func(d) or ffunc(d))):
        print("YES")
    else:
        print("NO")