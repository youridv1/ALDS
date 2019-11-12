def recGCD(a: int, b: int):
    if b == 0 or a == b:
        return a
    if a > b:
        return recGCD(b, a%b)

print(recGCD(24, 16))