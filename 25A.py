#25A - IQ test
import re
print([x.index(i)+1 for n in [[input()]] for x in [[int(i)%2 for i in re.split(" ",input())]] for i in [[x.count(0),x.count(1)].index(1)]][0])