#200B - Drinks
import re
n,s=int(input()),0
x=sum([int(i) for i in re.split(" ",input())])/n
print(round(x,12))