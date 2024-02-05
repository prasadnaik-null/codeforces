# 189A - Cut Ribbon
[n, a, b, c], ans = list(map(int, input().split())), 0
[a, b, c] = sorted([a, b, c])
for i in range(n//a, -1, -1):
    for j in range(0, (n//b)+1):
        if n < (a*i)+(b*j):
            break
        if (n-(a*i)-(b*j)) % c == 0:
            ans = max(i+j+(n-(a*i)-(b*j))//c, ans)
print(ans)