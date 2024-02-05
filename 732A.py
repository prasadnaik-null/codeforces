#732A - Buy a Shovel
import re
[k,r],i=[int(i) for i in re.split(" ",input())],1
while True:
  if str(k*i)[-1]=="0" or str(k*i)[-1]==str(r):
    print(i)
    break
  i+=1