def partition(l: list, lo: int, hi: int):
    pivot = l[hi]
    i = lo
    for j in range(lo, hi):
        if l[j] <= pivot:
            l[i], l[j] = l[j], l[i]
            i += 1
    l[i], l[hi] = l[hi], l[i]
    return i


def quickSort(l: list, lo: int, hi: int):
    if lo >= hi:
        return l
    p = partition(l, lo, hi)
    l = quickSort(l, lo, p-1)
    l = quickSort(l, p+1, hi)
    return l
    
l = [77, 22, 55, 33, 43, 99, 2, 0, 4]
print(quickSort(l, 0, len(l)-1))