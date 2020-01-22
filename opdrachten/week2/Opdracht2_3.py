import random
from datetime import datetime
random.seed(datetime.now())

def duplicate(l: list):
    """
    Function to find duplicates in a list

    PARAMETERS
    ===========
    l : list

    RETURN
    ===========
    result : bool


    EXAMPLE
    ===========
    >>> list = [3, 5, 4, 9, 12, 2, 3]
    >>> duplicate(list)
    True
    """
    l.sort()
    for i in range(1, len(l)):
        if l[i] == l[i-1]:
            return True
    return False



def birthdayProblem(n: int):
    """
    Function to calculate the chance of two people in a group of a given size 
    having the same birthday

    PARAMETERS
    ===========
    n: int

    RETURN
    ===========
    result : float
        the chance, in percentages, of two or more people having the same birthday
        in a given group after 100 of random samples of that groupsize.

    EXAMPLE
    ===========
    >>> birthdayProblem(23)
    50
    """
    count = 0
    for _ in range(100):
        l = []
        for _ in range(n):
            l.append(random.randrange(365))
        if(duplicate(l)):
            count += 1
    return count / 100.0

print(birthdayProblem(23))