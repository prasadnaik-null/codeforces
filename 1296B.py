# 1296B - Food Buying

def func(x):
    A, a, b = int(x), int(x), (x*1e17 - int(x)*1e17) / 1e17
    #print(A, a, b)
    while a > 0:
        A += a//10
        z = int(str(a)[-1])/10
        b += z
        # print(b)
        b = round(b*10)/10
        a //= 10
        #print(A, a, b, z)
    if b >= 1:
        return A+func(b)
    else:
        return A


for i in range(int(input())):
    print(func(int(input())))