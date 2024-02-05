#148A - Insomnia cure
l = [int(input()) for i in range(4)]
m = int(input())
print(len(set([i for i in range(1, m+1) for j in l if i % j == 0])))