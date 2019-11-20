class priorityQueue():
    def __init__(self):
        self.priorities = []

    def queue(self, v, p):
        if len(self.priorities) - 1 >= p:
            self.priorities[p].append(v)
        else:
            while len(self.priorities) - 1 < p:
                self.priorities.append([])
            self.priorities[p].append(v)
    
    def contains(self, v):
        for i in self.priorities:
            if i.contains(v):
                return True
        return False

    def dequeue(self):
        if self.priorities:
            for i in self.priorities:
                if i:
                    return i.pop()
        return None

    def remove(self, e):
       if self.priorities:
           for i in self.priorities:
               if i is not None:
                   while(e in i):
                       i.remove(e)

    def print(self):
        if self.priorities:
            for i in range(len(self.priorities)):
                if self.priorities[i]:
                    print(i, self.priorities[i])

l = priorityQueue()
l.queue(2, 0)
l.queue(2, 1)
l.queue(3, 1)
l.queue(4, 1)
l.queue(10, 10)
l.print()
print('\n')
l.remove(2)
l.print()
print(l.dequeue())
