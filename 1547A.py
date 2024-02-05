#1547A - Shortest Path with Obstacle
for i in range(int(input())):
  x,a,b,c=input(),list(map(int,input().split())),list(map(int,input().split())),list(map(int,input().split()))
  d=abs(a[0]-b[0])+abs(a[1]-b[1])
  if (a[0]==b[0] and a[0]==c[0] and c[1] in range(min(a[1],b[1]),max(a[1],b[1]))) or (a[1]==b[1] and a[1]==c[1] and c[0] in range(min(a[0],b[0]),max(a[0],b[0]))):
    print(d+2)
  else:
    print(d)