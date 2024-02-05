#1372B ~ prasadnaik-null
import math
for _ in range(int(input())):
    n=int(input())
    s,k=int(math.sqrt(n)),False
    for i in range(2,s+1):
        if n%i==0:
            x=n//i
            print(x,n-x)
            k=True
            break
    if k==False:
        print(1,n-1)