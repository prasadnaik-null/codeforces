# 1345A - Puzzle Pieces
for _ in range(int(input())):
    x = list(map(int, input().split()))
    if x[0] == 1 or x[1] == 1 or (x[0] == 2 and x[1] == 2):
        print("YES")
    else:
        print("NO")