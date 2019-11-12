def max(a: list):
    highScore = a[0]
    for i in a:
        if i > highScore:
            highScore = i
    return highScore


numbers = [1, 4, 5, 29, 307, 2, 0]

print(max(numbers))
