#THIS IS ALL WRONG BUT IT DOES WORK

class Node():
    def __init__(self, value = None):
        self.value = value
        self.tail = None


class linkedList():

    def __init__(self):
        self.tail = None

    def append(self, value):
        new = Node(value)
        if self.tail == None:
            self.tail = new
            return
        last = self.tail
        while(last.tail):
            last = last.tail
        last.tail = new

    def print(self):
        printvalue = self.tail
        while( printvalue is not None):
            print(printvalue.value)
            printvalue = printvalue.tail

    def delete(self, value):
            head = self.tail
            pre = self
            while head is not None:
                if head.value == value:
                    pre.tail = head.tail
                    head = pre.tail
                else:
                    pre = head
                    head = head.tail
            if head == None:
                return

l = linkedList()
l.append('first')
l.append('second')
l.append('third')
l.append('second')
l.append('second')
l.print()
print('\nremove all instances of second\n')
l.delete('second')
l.print()
