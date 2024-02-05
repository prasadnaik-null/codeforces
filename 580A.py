#580A - Kefa and First Steps
import re
n,s=int(input()),str()
x=[int(i) for i in re.split(" ",input())]
for i in range(len(x)-1):
  if x[i]<=x[i+1]:
    s+="1"
  else:
    s+="0"
y=sorted(re.findall("1*",s))[::-1][0]
print(len(str(y))+1)