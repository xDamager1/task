def read_file(file_path):
    with open(file_path, 'r') as h:
        ent = h.readline().strip().split()
    return ent

def f(a, index, tsum, csum, expr):
    if index == len(a):
        if csum == int(tsum):
            return expr
        return None

    result = f(a, index + 1, tsum, csum + int(a[index]), expr + '+' + a[index] if index > 0 else a[index])

    if result:
        return result

    result = f(a, index + 1, tsum, csum - int(a[index]), expr + '-' + a[index])
    return result

def main():
    global f
    ent = read_file('input.txt.txt')
    a = ent[1:len(ent) - 1]
    tsum = ent[-1]
    b = f(a, 0, tsum, 0, '')
    if b:
        with open('output.txt', 'w') as f:
            f.write(b + '=' + tsum)
    else:
        with open('output.txt', 'w') as f:
            f.write('No solution')

if __name__ == "__main__":
    main()