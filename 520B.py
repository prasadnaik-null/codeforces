# 520B - Two Buttons
def func(f, i):
    if i < (f+1)//2:
        if f % 2 == 0:
            return func((f)//2, i)+1
        else:
            return func((f+1)//2, i)+2
    if i > f:
        return i-f
    elif i*2 == f:
        return 1
    elif i*2 > f+1:
        z = (f+1)//2
        return func(f, z)+i-z
    else:
        return func(f, i*2)+1


[i, f] = list(map(int, input().split()))
print(func(f, i))