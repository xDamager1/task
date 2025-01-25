
a = input()
if ((int(a) > 0) and (int(a) <= 128)) and (int(a[-1] + a[:-1]) <= 128):
    if len(a) == 3:
        if (a[-1] == '0') and (a[1] == '0'):
            print(a[0])
    else:
        if len(a) == 2:
            if a[1] == '0':
                print(a[0])
            else:
                print(a[-1] + a[:-1])
elif ((int(a) < 0) and (int(a) >= -128)) and (int('-' + a[-1] + a[1:-1]) >= -128):
    if len(a) == 4:
        if (a[-1] == '0') and (a[2] == '0'):
            print('-' + a[1])
        else:
            print('-' + a[-1] + a[2] + a[1])
    else:
        if a[-1] == '0':
            print('-' + a[1:-1])
        else:
            print('-' + a[-1] + a[1:-1])
else:
    print('No solution')
