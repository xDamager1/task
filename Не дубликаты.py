def f(list1, list2):
    list1 = set()
    list2 = set()
    a1 = f'{len(list1 & list2)} элемента, {list(list1 & list2)}'
    a2 = f'{len(list1 ^ list2)} элементов, {list(list1 ^ list2)}'
    a3 = f'{len(list1 - list2)} элементов, {list(list1 - list2)}'
    a4 = f'{len(list2 - list1)} элементов, {list(list2 - list1)}'
    return a1, a2, a3, a4


list1 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25]
list2 = [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]
print(f(list1, list2))