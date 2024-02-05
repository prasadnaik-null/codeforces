#344A - Magnets
n=int(input())
j=1
for i in range(n):
  m=input()
  if i!=0 and m!=c:
    c=m
    j+=1
  else:
    c=m
print(j)