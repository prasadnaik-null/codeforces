#520A - Pangram
print("YES" if 0 not in [z for n in [int(input())] for x in [input().lower()] for i in range(97,123) for z in [x.count(chr(i))]] else "NO")