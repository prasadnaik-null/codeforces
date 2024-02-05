#1400A - String Similarity
import re
for i in range(int(input())):
  x,n=int(input()),input()
  z=(2**x)
  for j in range(z):
    y=bin(z-j-1)[2:]
    a=bin(j)[2:]
    if len(re.findall("0"*(x-len(y))+y,n))==0:
      print("0"*(x-len(a))+a)
      break