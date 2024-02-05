#163A - Stones on the Table
n=int(input())
x=input()
m=0
for i in range(n-1):
  if x[i]==x[i+1]:
    x=x[:n]+x[n+1:]
    m+=1
print(m)