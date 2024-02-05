# 467B - Fedor and New Game
[n, m, k], l, a = list(map(int, input().split())), [], 0
for i in range(m+1):
    l.append(int(input()))
j = l[-1]


def solve(A, B):
    XOR = A ^ B
    count = 0
    # Check for 1's in the binary form using
    # Brian Kernighan's Algorithm
    while (XOR):
        XOR = XOR & (XOR - 1)
        count += 1
    return count


for i in l[:-1]:
    if solve(i, j) <= k:
        a += 1
print(a)