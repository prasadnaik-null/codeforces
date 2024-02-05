#1030A - In Search of an Easy Problem
import re
n=int(input())
x=[int(i) for i in re.split(" ",input())]
if 1 in x:
  print("HARD")
else:
  print("EASY")