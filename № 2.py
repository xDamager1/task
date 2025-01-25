a = input()
if len(a) % 2 == 0:
    if a[:(len(a) // 2)] == (a[-1] + a[(len(a) // 2):-1]):
        print(True)
    else:
        print(False)
if len(a) % 2 != 0:
    if a[:(len(a) // 2)] == (a[-1] + a[(len(a) // 2 + 1):-1]):
        print(True)
    else:
        print(False) 