# 734B - Anton and Digits
[a, b, c, d] = list(map(int, input().split()))
print((min(a, c, d)*256)+(min(a-min(a, c, d), b)*32))