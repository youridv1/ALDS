class linkedList():
    """
    Class to make a linked list

    EXAMPLE
    ===========
    >>> list = Linkedlist() (first element is None)
    >>> list = Linkedlist(1)(first element is 1)
    """
    def __init__(self, value = None):
        """
        Construct for linkedList

        PARAMETERS
        ===========
        self : self
        value : anything

        EXAMPLE
        ===========
        >>> list = Linkedlist() (first element is None)
        >>> list = Linkedlist(1)(first element is 1)
        """
        self.value = value
        self.tail = None

    def append(self, value):
        """
        Function to append to a linked list

        PARAMETERS
        ============
        self : self
        value : anything

        EXAMPLE
        ============
        >>> llist = linkedList(1)
        >>> llist.append(2)
        """
        if self.tail == None:
            self.tail = linkedList(value)
        else:
            self.tail.append(value)

    def print(self):
        """
        Function to print a linked list

        PARAMETERS
        ============
        self : self

        EXAMPLE
        ============
        >>> llist = linkedList(1)
        >>> l = linkedList(1)
        >>> l.append(2)
        >>> l.append(3)
        >>> l.append(0)
        >>> l.append(5)
        >>> l.append(6)
        >>> l.delete(0)
        >>> llist.print()
        1
        2
        3
        5
        6
        """
        print(self.value)
        if self.tail:
            self.tail.print()

    def delete(self, value, prev = None):
        """
        Function to delete a value from a linked list

        PARAMETERS
        ============
        value : anything

        EXAMPLE
        ============
        >>> llist.delete(2)
        """
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
        """
        Function to return the minimum value of a linked list

        PARAMETERS
        ============
        value : anything

        EXAMPLE
        ============
        llist.delete(2)
        """"""
        Function to delete a value from a linked list

        PARAMETERS
        ============
        value : anything

        EXAMPLE
        ============
        >>> llist = linkedList(1)
        >>> l = linkedList(1)
        >>> l.append(2)
        >>> l.append(3)
        >>> l.append(0)
        >>> l.append(5)
        >>> l.append(6)
        >>> l.delete()
        >>> llist.min()
        0
        """
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