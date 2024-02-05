#1283A - Minutes Before the New Year
import re
for i in range(int(input())):
  [h,m]=[int(i) for i in re.split(" ",input())]
  print(((24-h)*60)-m)