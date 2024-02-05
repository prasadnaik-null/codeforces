#1358A - Park Lighting
import re
for i in range(int(input())):
  [n,m]=[int(i) for i in re.split(" ",input())]
  print(((n*m)+1)//2)