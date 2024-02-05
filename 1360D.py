# 1360D - Buying Shovels
def factors(n, k):
    l = [1]
    lx = [n]
    c = True
    for i in range(1, int(n**0.5)+1):
        if i <= k:
            if n % i == 0:
                l.append(i)
                lx.append(n//i)
        else:
            c = False
            break
    if c == False:
        print(lx[-1])
    else:
        if lx[-1] > k:
            print(lx[-1])
        else:
            y=True
            for i in lx[::-1]:
                if i > k:
                    print(l[lx.index(x)])
                    y=False
                    break
                x = i
            if y==True:
                print(l[lx.index(x)])


for _ in range(int(input())):
    [n, k] = list(map(int, input().split()))
    factors(n, k)