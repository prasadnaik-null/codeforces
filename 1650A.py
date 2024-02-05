# 1650A - Deletions of Two Adjacent Letters
for _ in range(int(input())):
    a, b, k = input(), input(), False
    for i in range(len(a)):
        if a[i] == b and i % 2 == 0:
            print("YES")
            k = True
            break
    if k == False:
        print("NO")