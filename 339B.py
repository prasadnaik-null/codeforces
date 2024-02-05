#339B - Xenia and Ringroad
import re
print(sum([c for n in [[int(i) for i in re.split(" ",input())]] for x in [[1]+[int(i) for i in re.split(" ",input())]] for i in range(n[1]) for c in [(x[i+1]-x[i] if x[i]<=x[i+1] else n[0]-x[i]+x[i+1])]]))