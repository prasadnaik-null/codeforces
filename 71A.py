#65A - Way too long words
n=int(input())
i=1
for i in range(n):
  x=input()
  if len(x)>10:
    print(x[0]+str(len(x)-2)+x[len(x)-1])
  else:
    print(x)