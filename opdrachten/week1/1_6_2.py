import timeit

mysetup = '''
def mean(t):
    sum = 0
    for i in t:
        sum += i
    return sum / len(t)
'''
    
mycode = '''
def hairy(l: list):
    totalAverage = mean(l)
    result = []
    for i in range(0, len(l)):
        for j in range(i+1, len(l)):
            for k in range(j+1, len(l)):
                tup = (l[i], l[j], l[k])
                relativeHair = mean(tup) - totalAverage
                item = (tup, relativeHair)
                result.append(item)
    return result

lijst = [20, 25, 30, 35]

hairy(lijst)

'''
print (timeit.timeit(setup = mysetup, stmt = mycode, number = 1000000))
