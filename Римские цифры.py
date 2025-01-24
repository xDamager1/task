def f(s):
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    c = 0
    for i in range(len(s)):
        c += a[s[i]]
    for j in range(len(s) - 1):
        if s[j] == 'I' and s[j + 1] == 'V':
            c = c - 2
        elif s[j] == 'I' and s[j + 1] == 'X':
            c = c - 2
        elif s[j] == 'X' and s[j + 1] == 'L':
            c = c - 20
        elif s[j] == 'X' and s[j + 1] == 'C':
            c = c - 20
        elif s[j] == 'C' and s[j + 1] == 'D':
            c = c - 200
        elif s[j] == 'C' and s[j + 1] == 'M':
            c = c - 200

    return c


s = input()
print(f(s))