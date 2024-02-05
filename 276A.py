# 276A -p(int, input().split())), Lunch Rush
[n, k] = list(map(int, input().split()))
x = list(map(int, input().split()))
if x[1] > k:
    l = x[0]+k-x[1]
else:
    l = x[0]
for i in range(n-1):
    [f, t] = list(map(int, input().split()))
    if t > k:
        z = f+k-t
    else:
        z = f
    l = z if z > l else l
print(l)