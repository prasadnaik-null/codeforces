#1325A - CopyCopyCopyCopyCopy
import re
for i in range(int(input())):
  n=int(input())
  print(len(list(set([int(i) for i in re.split(" ",input())]))))