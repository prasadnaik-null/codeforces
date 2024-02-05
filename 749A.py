#749A - Bachgold Problem
n=int(input())
a=n//2
print(a)
if n%2==0:
  print(*([2]*a))
else:
  print(*([2]*(a-1)+[3]))