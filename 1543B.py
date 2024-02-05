# 1543B - Customising the Track

for _ in range(int(input())):
    n, l = int(input()), sum(list(map(int, input().split())))
    x = l % n
    print(x*(n-x))