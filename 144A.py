#144A - Arrival of the General
import re
n,x=int(input()),[int(i) for i in re.split(" ",input())]
y=x.index(max(x))
x=([max(x)]+x[:x.index(max(x))]+x[x.index(max(x))+1:])[::-1]
y+=x.index(min(x))
print(y)