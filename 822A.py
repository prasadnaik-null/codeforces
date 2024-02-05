# 822A - I'm bored with life
def fact(x):
    a = 1
    for i in range(1, x+1):
        a *= i
    return a


[x, y] = list(map(int, input().split()))
print(fact(min(x, y)))