#1337B - Kana and Dragon Quest game
for i in range(int(input())):
  [a,b,c]=list(map(int,input().split()))
  while True:
    v,l=(a//2)+10,a-10
    if a<=10*c:
      a-=10*c
    elif b>0:
      a=v
      b-=1
    elif c>0:
      a=l
      c-=1
    if a<=0:
      print("YES")
      k=True
      break
    if b==0 and c==0:
      k=False
      break
  if k==False:
    print("NO")