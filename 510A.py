#510A - Fox And Snake
import re
n=[int(i) for i in re.split(" ",input())]
for i in range(n[0]):
  if (i+1)%4==0:
    print('#'+'.'*(n[1]-1))
  elif (i+1)%2==0:
    print('.'*(n[1]-1)+'#')
  else:
    print('#'*n[1])