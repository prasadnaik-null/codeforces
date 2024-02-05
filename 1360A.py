#1360A - Minimal Square
import re
for i in range(int(input())):
  [a,b]=sorted([int(i) for i in re.split(" ",input())])
  print(max(a*2,b)**2)