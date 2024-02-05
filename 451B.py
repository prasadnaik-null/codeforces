# 451B - Sort the Array
n, l = int(input()), list(map(int, input().split()))
x, i, f = l[:], None, n
for j in range(1, n):
    if i == None:
        if l[j] < l[j-1]:
            i = j-1
    else:
        if l[j] > l[j-1]:
            f = j
            break
if i != None:
    x = l[:i]+l[i:f][::-1]+l[f:]
    if x == sorted(l):
        print("yes")
        print(i+1, f)
    else:
        print("no")
else:
    print("yes")
    print(1, 1)