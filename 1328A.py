#1328A - Divisibility Problem(k for i in range(int(input())) for j
import re
print(*[(x[1]-x[0]%x[1])%x[1] for j in range(int(input())) for x in [[int(i) for i in re.split(" ",input())]]], sep = "\n")