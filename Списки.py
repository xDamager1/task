import itertools
a = [1, 1, 2]
b = []
c = []
c1 = []
b = itertools.permutations(a)
for i in b:
    c.append(list(i))
for j in c:
    if j not in c1:
        c1.append(j)
print(c1)