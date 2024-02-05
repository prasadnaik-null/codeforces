# 156A - Message
x, y = input(), input()
z = len(y)
x = "0"*z+x+"0"*z
m = 0
for i in range(len(x)-z):
    w = x[i:i+z]
    a = 0
    for j in range(z):
        if w[j] == y[j]:
            a += 1
    m = max(m, a)
print(z-m)