def zigzag(m, n):
    if n == 1:
        return m
    rs = [''] * n
    l, step = 0, 1
    for k in m:
        rs[l] += k
        if l == 0:
            step = 1
        elif l == n - 1:
            step = -1
        l += step
    return "".join(rs)
m = input("")
n = int(input())
print(zigzag(m, n))