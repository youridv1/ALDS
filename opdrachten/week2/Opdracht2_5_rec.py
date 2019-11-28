class linkedList():
    def __init__(self, value = None):
        self.value = value
        self.tail = None

    def append(self, value):
        if self.tail == None:
            self.tail = linkedList(value)
        else:
            self.tail.append(value)

    def print(self):
        print(self.value)
        if self.tail:
            self.tail.print()

    def delete(self, value, prev = None):
        if prev == None:
            if self.value == value:
                self.value = self.tail.value
                self.tail = self.tail.tail
                self.delete(value)
            self.tail.delete(value, self)
        elif self.tail == None:
            if self.value == value:
                prev.tail = None
        elif self.value == value:
            prev.tail = self.tail
            prev.tail.delete(value, prev)
        else:
            self.tail.delete(value, self)

    def min(self):
        if self.tail == None:
            return self.value
        tmp = self.tail.min()
        if tmp < self.value:
            return tmp
        return self.value
        




l = linkedList(1)
l.append(2)
l.append(3)
l.append(0)
l.append(5)
l.append(6)
l.delete(0)
l.print()