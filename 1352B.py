# 1352B - Same Parity Summands
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    if n >= k:
        if n % 2 == 1:
            if k % 2 == 0:
                print("NO")
            else:
                print("YES")
                print("1 "*(k-1)+str(n-k+1))
        else:
            if k % 2 == 0:
                print("YES")
                print("1 "*(k-1)+str(n-k+1))
            else:
                if n >= k*2:
                    print("YES")
                    print("2 "*(k-1)+str(n-2*(k-1)))
                else:
                    print("NO")
    else:
        print("NO")