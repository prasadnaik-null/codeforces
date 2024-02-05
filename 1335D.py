# 1335D - Anti-Sudoku
for _ in range(int(input())):
    for i in range(3):
        x = input()
        y = i*3
        if x[y] != "9":
            print(x[0:y]+str(int(x[y])+1)+x[y+1:])
        else:
            print(x[0:y]+"1"+x[y+1:])
    for i in range(3):
        x = input()
        y = (i*3)+1
        if x[y] != "9":
            print(x[0:y]+str(int(x[y])+1)+x[y+1:])
        else:
            print(x[0:y]+"1"+x[y+1:])
    for i in range(3):
        x = input()
        y = (i*3)+2
        if x[y] != "9":
            print(x[0:y]+str(int(x[y])+1)+x[y+1:])
        else:
            print(x[0:y]+"1"+x[y+1:])