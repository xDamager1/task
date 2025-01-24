from itertools import combinations


def f(elem):
    ue = set(elem)
    subsets = []

    for r in range(1, len(ue) + 1):
        subsets.extend(combinations(ue, r))

    return subsets


list1 = [1, 2, 3, 4]
s1 = f(list1)
print("Подмножества:", s1)
print("Количество подмножеств:", len(s1))

list2 = ['a', 'b', 'c', 'd', 'd']
s2 = f(list2)
print("Подмножества:", s2)
print("Количество подмножеств:", len(s2))