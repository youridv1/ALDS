def isPrime(n: int):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True

def findPrime(bound: int):
    result = []
    for i in range(2, bound, 1):
        if(isPrime(i)):
            result.append(i)
    return result

print(findPrime(1000))