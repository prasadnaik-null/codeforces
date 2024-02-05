#492A - Vanya and Lanterns
import re
print(f'{max([c for n in [[int(i) for i in re.split(" ",input())]] for x in [sorted([int(i) for i in re.split(" ",input())]+[0,n[1]])] for j in range(n[0]+1) for c in [(x[j+1]-x[j])*(2 if j==0 or j==n[0] else 1)]])/2:.10f}')