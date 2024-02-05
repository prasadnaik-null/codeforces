#1473A - Replacing Elements
for i in range(int(input())):
  [n,d],x=list(map(int,input().split())),sorted(list(map(int,input().split())))
  print("YES" if sum(x[:2])<=d or x[-1]<=d else "NO")