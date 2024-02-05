# 82A - Double Cola
import math
n = int(input())
x = (n-1)//5
y = int(math.log((x+1), 2))
n -= 5*((2**y)-1)+1
n //= (2**y)
d = {0: "Sheldon", 1: "Leonard", 2: "Penny", 3: "Rajesh", 4: "Howard"}
print(d[n])