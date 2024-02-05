# 1238A - Prime Subtraction
for _ in range(int(input())):
    [x,y]=list(map(int, input().split()))
    if x-y==1:
        print("NO")
    else:
        print("YES")