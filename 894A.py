# 894A - QAQ
x, q, a = input(), [], 0
for i in range(len(x)):
    if x[i] == "Q":
        q.append(i)
for i in q:
    for j in q:
        if j > i:
            a += x[i:j+1].count("A")
print(a)