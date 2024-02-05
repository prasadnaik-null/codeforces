#337A - Puzzles
import re
print(min([z[-1]-z[0] for x in [[int(i) for i in re.split(" ",input())]] for y in [sorted([int(i) for i in re.split(" ",input())])] for i in range(x[1]-x[0]+1) for z in [y[i:i+x[0]]]]))