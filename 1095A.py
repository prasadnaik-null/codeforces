# 1095A - Repeating Cipher
n, s = int(input()), input()
k, l, z = 0, 1, ''
while k+1 <= n:
    z += s[k]
    l, k = l+1, k+l
print(z)