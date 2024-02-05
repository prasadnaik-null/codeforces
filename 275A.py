# 275A - Lights Out
def lol(x):
    if x == 1:
        return 0
    else:
        return 1


l = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [
    1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
m = [[0, 0, 0, 0, 0]]
for i in range(3):
    m.append([0]+list(map(int, input().split()))+[0])
m.append([0, 0, 0, 0, 0])
for i in range(1, 4):
    for j in range(1, 4):
        if m[i][j] % 2 == 1:
            l[i][j-1] = (l[i][j-1]+1) % 2
            l[i][j+1] = lol(l[i][j+1])
            l[i-1][j] = lol(l[i-1][j])
            l[i+1][j] = lol(l[i+1][j])
            l[i][j] = lol(l[i][j])
for i in range(1, 4):
    print(*l[i][1:4], sep='')