# 1324B - Yet Another Palindrome Problem
for _ in range(int(input())):
    n, l, k = int(input()), list(map(int, input().split())), False
    for i in range(n):
        if l[i:].count(l[i]) == 2:
            if l[i+1] != l[i]:
                print("YES")
                k = True
                break
        elif l.count(l[i]) > 2:
            print("YES")
            k = True
            break
    if k == False:
        print("NO")