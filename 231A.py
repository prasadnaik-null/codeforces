#143A - Team
import re
n=int(input())
count=0
for i in range(n):
  x=input()
  if len(re.findall("1",x))>=2:
    count+=1
print(count)