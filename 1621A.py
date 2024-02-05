# 1621A - Stable Arrangement of Rooks
for _ in range(int(input())):
    [n, k], c = list(map(int, input().split())), 0
    if k > (n+1)//2:
        print(-1)
    else:
        for i in range(n):
            if i % 2 == 1:
                print("."*n)
            else:
                if c < k:
                    print("."*(i)+"R"+"."*(n-i-1))
                    c += 1
                else:
                    print("."*n)