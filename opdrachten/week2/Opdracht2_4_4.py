from statistics import median

def partition(l: list, lo: int, hi: int):
    if hi <= lo:
        return l, 0
    pivot = median(l[lo:hi])
    ind = l.index(pivot)
    l[hi], l[ind] = l[ind], l[hi]
    pivot = l[hi]
    #print(l)
    i = lo
    cmp = 0
    for j in range(lo, hi):
        cmp += 1
        if l[j] <= pivot:
            l[i], l[j] = l[j], l[i]
            i += 1
    l[i], l[hi] = l[hi], l[i]
    print(l)
    return i, cmp


def quickSort(l: list, lo: int, hi: int):
    cmp = [None] * 3
    if lo >= hi:
        return l, 1
    p, cmp[0] = partition(l, lo, hi)
    print(p)
    l, cmp[1] = quickSort(l, lo, p-1)
    l, cmp[2] = quickSort(l, p+1, hi)
    return l, sum(cmp)+1
    
l = [77, 22, 55, 33, 43, 99, 2, 0, 4]
l, cmp = quickSort(l, 0, len(l)-1)
print(l)
print(cmp)