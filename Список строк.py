a = ["a", "a", ""]
def f(x):
    z = {}
    for y in x:
        key = (len(y), ''.join(sorted(y)))
        z.setdefault(key, []).append(y)
    return list(z.values())
print(f(a))