a = '(]'
for i in a:
    if '()' in a:
        a = a.replace('()', '12')
    if ('(1' in a) and ('2)' in a):
        a = a.replace('(1', '11')
        a = a.replace('2)', '22')
    if ('(3' in a) and ('4)' in a):
        a = a.replace('(3', '13')
        a = a.replace('4)', '42')
    if ('(5' in a) and ('6)' in a):
        a = a.replace('(5', '15')
        a = a.replace('6)', '62')
    if '[]' in a:
        a = a.replace('[]', '34')
    if ('[3' in a) and ('4]' in a):
        a = a.replace('[3', '33')
        a = a.replace('4]', '44')
    if ('[1' in a) and ('2]' in a):
        a = a.replace('[1', '31')
        a = a.replace('2]', '24')
    if ('[5' in a) and ('6]' in a):
        a = a.replace('[5', '35')
        a = a.replace('6]', '64')
    if '{}' in a:
        a = a.replace('{}', '56')
    if ('{5' in a) and ('6}' in a):
        a = a.replace('{5', '55')
        a = a.replace('6}', '66')
    if ('{1' in a) and ('2}' in a):
        a = a.replace('{1', '51')
        a = a.replace('2}', '26')
    if ('{3' in a) and ('4}' in a):
        a = a.replace('{3', '53')
        a = a.replace('4}', '46')
if ('{' not in a) and ('}' not in a) and ('[' not in a) and (']' not in a) and ('(' not in a) and (')' not in a):
    print('True')
elif ('1' not in a) and ('2' not in a) and ('3' not in a) and ('4' not in a) and ('5' not in a) and ('6' not in a):
    print('False')
elif ((a[0] == '{') or (a[0] == '[') or (a[0] == '(')) and ((a[-1] == ']') or (a[-1] == '}') or (a[-1] == ')')) and (
        (a.count('[') + a.count(']') + a.count('(') + a.count(')') + a.count('{') + a.count('}')) == 2):
    print('True')
elif ((a[-1] == ']') or (a[-1] == '}') or (a[-1] == ')')) and ((a.count(')') + a.count('{') + a.count('}')) == 1):
    print('True')
else:
    if ((a[0] == '[') or (a[0] == '{') or (a[0] == '(')) and ((a[-1] == ')') or (a[-1] == '}') or (a[-1] == ']')) and (
            a[0] != a[-1]):
        a = a.replace('{', '_')
        a = a.replace('}', '_')
        a = a.replace('(', '_')
        a = a.replace(')', '_')
        a = a.replace('[', '_')
        a = a.replace(']', '_')
        a = a.replace('1', '(')
        a = a.replace('2', ')')
        a = a.replace('3', '[')
        a = a.replace('4', ']')
        a = a.replace('5', '{')
        a = a.replace('6', '}')
        a = a.split('_')
        m = 0
        k = 0
        for i in a:
            for j in i:
                k += 1
                m = max(m, k)
            k = 0
            if len(i) == m:
                print(i)
    else:
        a = a.replace('{', '_')
        a = a.replace('}', '_')
        a = a.replace('(', '_')
        a = a.replace(')', '_')
        a = a.replace('[', '_')
        a = a.replace(']', '_')
        a = a.replace('1', '(')
        a = a.replace('2', ')')
        a = a.replace('3', '[')
        a = a.replace('4', ']')
        a = a.replace('5', '{')
        a = a.replace('6', '}')
        a = a.split('_')
        m = 0
        k = 0
        for i in a:
            for j in i:
                k += 1
                m = max(m, k)
            k = 0
            if len(i) == m:
                print(i)
