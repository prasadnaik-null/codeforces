# 768A - Oath of the Night's Watch
n, l = int(input()), sorted(list(map(int, input().split())))
print(n-l.count(l[0])-l.count(l[-1])) if l[0]!=l[-1] else print(0)