# 1196A - Three Piles of Candies
for _ in range(int(input())):
    [a, b, c] = sorted(list(map(int, input().split())))
    d = b-a
    print(b+(c-d)//2)