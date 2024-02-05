#1475A - Odd Divisor
import math
for i in range(int(input())):
  print("NO" if math.log(int(input()),2)%1==0 else "YES")