#1154A - Restoring Three Numbers 
import re
[a,b,c,d]=sorted([int(i) for i in re.split(" ",input())])
print(*[d-c,d-b,d-a])