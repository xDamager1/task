n = int(input())
c = int(input())
a = []
r = 1000000
for i in range(n):
    x = int(input())
    a.append(x)
for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            for x in range(len(a)):
                if i != j and i != k and i != x and j != k and j != x and k != x:
                    s = a[i] + a[j] + a[k] + a[x]
                    if abs(s - c) < r:
                        r = abs(s - c)
                        b = []
                        b.append(a[i])
                        b.append(a[j])
                        b.append(a[k])
                        b.append(a[x])
                    else:
                        break
print(b)
print(sum(b))