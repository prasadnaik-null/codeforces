#1551B1 - Wonderful Coloring - 1
for i in range(int(input())):
  x,y,r,g=input(),{},0,0
  for i in x:
    try:
      y[i]+=1
      if y[i]>2:
        pass
      elif r>g:
        g+=1
      else:
        r+=1
    except:
      if r>g:
        g+=1
      else:
        r+=1 
      y[i]=1
  print(g)