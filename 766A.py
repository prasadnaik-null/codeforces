# 766A - Mahmoud and Longest Uncommon Subsequence
x, y = input(), input()
if x == y:
    print(-1)
else:
    print(max(len(x), len(y)))