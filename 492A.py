#492A - Vanya and Cubes
n,i,s=int(input()),1,0
while True:
  s+=(i*(i+1))//2
  if s>n:
    print(i-1)
    break
  i+=1