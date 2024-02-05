#978A - File Name
import re
n,x,m=int(input()),input(),0
y=re.findall("xxx+",x)
for i in y:
  m+=len(i)-2
print(m)