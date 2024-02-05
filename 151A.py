#151A - Soft Drinking
import re
[n, k, l, c, d, p, nl, np]=[int(i) for i in re.split(" ",input())]
print(min((k*l)//nl,c*d,p//np)//n)