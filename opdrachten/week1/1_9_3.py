def sieveOfEratosthenes(bound: int):
    candidates = set()
    for i in range(2, bound, 1):
        candidates.add(i)
    composites = set()
    for j in range(2, bound, 1):
        for k in range(2, int(bound/j+1), 1):
            comp = j * k
            composites.add(comp)
    primes = candidates.difference(composites)
    return primes

print(sieveOfEratosthenes(1000))