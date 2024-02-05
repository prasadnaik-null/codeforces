# 1560C - Infinity Table
import math
for _ in range(int(input())):
    x = int(input())
    y = math.ceil(math.sqrt(x))
    if x > (y**2)-y:
        print(y, (y**2)-x+1)
    else:
        print(x-((y-1)**2), y)