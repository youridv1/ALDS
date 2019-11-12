def pseudoLoop(l: list, max: int):
    result = []
    for i in range(0, int((len(l)/2))):
        j = len(l)-1-i
        sum = 0
        for k in range(i, j):
            sum += l[k]
        if sum > max:
            sum = max
        result.append(sum)
    return result


test = [1, 10, 9, 78, 40, 23, 30, 2, 1]
max = 200

print(pseudoLoop(test, max))
print(sum(test))
