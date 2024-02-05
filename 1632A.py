# 1632A - ABC
for _ in range(int(input())):
    x, y, k = int(input()), input(), False
    for i in range(x-1):
        for j in range(x, i+1, -1):
            z = y[i:j]
            if z == z[::-1]:
                k = True
                print("NO")
                break
        if k == True:
            break
    if k == False:
        print("YES")