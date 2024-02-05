#1343A - Candies
for i in range(int(input())):
  x,i,j=int(input()),2,3
  while True:
    if x%j==0:
      print(x//j)
      break
    else:
      j+=(2**i)
      i+=1