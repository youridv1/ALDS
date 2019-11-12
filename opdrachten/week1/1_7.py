def recFind(l: list, x):
    if len(l) == 0:
        return -1
    if l[-1] == x:
        return len(l) - 1
    return recFind(l[:-1], x)

l = [0, 1, 2, 3, 4, 5]
print(recFind(l, 3))