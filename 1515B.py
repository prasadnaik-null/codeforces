# 1515B - Phoenix and Puzzle
import math

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print("NO")
    elif 2**round(math.log2(n)) == n:
        print("YES")
    else:
        i = 0
        while True:
            if n/2 % 1 == 0:
                n /= 2
                i = 1
            else:
                break
        if math.sqrt(n) == int(math.sqrt(n)) and i:
            print("YES")
        else:
            print("NO")