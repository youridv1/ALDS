import timeit
    
mycode = '''
def hairy(l: list):
    total = sum(l)
    length = len(l)
    result = []
    for i in range(0, len(l)):
        for j in range(i+1, len(l)):
            for k in range(j+1, len(l)):
                tup = (l[i], l[j], l[k])
                relativeHair = sum(tup)/3 - (total - sum(tup))/(length - 3)
                item = (tup, relativeHair)
                result.append(item)
    return result

lijst = [20, 25, 30, 35]

hairy(lijst)

'''
print (timeit.timeit(stmt = mycode, number = 1000000))
