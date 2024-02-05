#467A - George and Accommodation
import re
n=int(input())
j=0
for i in range(n):
  x=[int(i) for i in re.split(" ",input())]
  if x[0]+1<x[1]:
    j+=1
print(j)