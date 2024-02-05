# 746B - Decoding
n, s = int(input()), input()
a = [0]*n
if n % 2 == 1:
    a[n//2] = s[0]
    for i in range(n//2):
        a[(n//2)-i-1] = s[(2*i)+1]
        a[(n//2)+i+1] = s[(2*i)+2]
else:
    for i in range(n//2):
        a[(n//2)-i-1] = s[2*i]
        a[(n//2)+i] = s[(2*i)+1]
print(*a, sep="")