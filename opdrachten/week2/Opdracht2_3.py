import random
from datetime import datetime
random.seed(datetime.now())

def duplicate(l: list):
    """
    
    """
    l.sort()
    for i in range(1, len(l)):
        if l[i] == l[i-1]:
            return True
    return False


def birthdayProblem(n: int):
    count = 0
    for _ in range(100):
        l = []
        for _ in range(n):
            l.append(random.randrange(365))
        if(duplicate(l)):
            count += 1
    return count / 100.0

print(birthdayProblem(23))