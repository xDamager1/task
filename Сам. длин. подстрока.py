s = str(input())
m = 0
k = 0
h = 0
d = set()
while (h < len(s)) and (k < len(s)):
    if s[k] not in d:
        d.add(s[k])
        k += 1
        m = max(m, k - h)
    else:
        d.remove(s[h])
        h += 1
print(m)