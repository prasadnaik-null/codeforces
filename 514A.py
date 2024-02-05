# 514A - Chewbaca and Number
n = input()
x = ""
y = int(n[0])
if y >= 5 and y != 9:
    x += str(9-y)
else:
    x += n[0]
for i in range(1, len(n)):
    y = int(n[i])
    if y >= 5:
        x += str(9-y)
    else:
        x += n[i]
print(x)