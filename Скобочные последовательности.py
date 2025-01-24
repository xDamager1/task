def f(n):
    result = []

    def g(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        if open_count < n:
            g(current + '(', open_count + 1, close_count)
        if close_count < open_count:
            g(current + ')', open_count, close_count + 1)

    g('', 0, 0)
    return result

n = 3
a = f(n)
print("Все правильные скобочные последовательности:")
print(a)