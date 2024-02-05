# 255A - Greg's Workout
n, l, c, bi, ba = int(input()), list(map(int, input().split())), 0, 0, 0
for i in range(n):
    if i % 3 == 0:
        c += l[i]
    elif i % 3 == 1:
        bi += l[i]
    else:
        ba += l[i]
m = max(c, bi, ba)
if c == m:
    print("chest")
elif bi == m:
    print("biceps")
else:
    print("back")