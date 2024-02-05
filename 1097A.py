#1097A - Gennady and a Card Game
import re
x,y,z=input(),input(),[]
z=re.findall(rf"{x[0]}",y)+re.findall(rf"{x[1]}",y)
if z!=[]:
  print("YES")
else:
  print("NO")