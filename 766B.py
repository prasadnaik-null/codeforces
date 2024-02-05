# 766B - Mahmoud and a Triangle
n, l, k = int(input()), sorted(list(map(int, input().split()))), False
for i in range(n-2):
    if l[i+2] < l[i+1]+l[i]:
        print("YES")
        k = True
        break
if k == False:
    print("NO")