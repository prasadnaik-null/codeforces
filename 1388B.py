# 1388B - Captain Flint and a Long Voyage
from math import ceil
for _ in range(int(input())):
    n=int(input())
    d=ceil(n/4)
    print("9"*(n-d)+"8"*d)