#581A - Vasya the Hipster
import re
print(*[i for [r,b] in [[int(i) for i in re.split(" ",input())]] for i in [min(r,b),(max(r,b)-min(r,b))//2]])