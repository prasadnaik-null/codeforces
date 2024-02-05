#996A - Hit the Lottery
print(sum([c for z in [int(input())] for d in [[100,20,10,5,1]] for n in range(5) for c in [z//d[n]] for z in [z-c*d[n]]]))