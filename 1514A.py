# 1514A - Perfectly Imperfect Array
import math
from xml.etree.ElementTree import TreeBuilder
for _ in range(int(input())):
    n, l, k = int(input()), list(map(int, input().split())), True
    for i in l:
        if math.sqrt(i) % 1 != 0:
            print("YES")
            k = False
            break
    if k == True:
        print("NO")