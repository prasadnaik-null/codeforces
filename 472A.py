#472A - Design Tutorial: Learn from Math
def isC(n):
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return True
  return False

n=int(input())
for i in range(4,(n//2)+1):
  if isC(i) and isC(n-i):
    print(i,n-i)
    break