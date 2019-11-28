class myStack():
    """
    Class to make a stack

    EXAMPLE
    ===========
    >>> stack = myStack
    """

    def __init__(self):
        """
        Construct for Class myStack

        PARAMETERS
        ===========
        self : self

        EXAMPLE
        ===========
        >>> stack = myStack
        """
        self.list = []

    def isEmpty(self):
        """
        Function to check if the stack is empty

        PARAMETERS
        ===========
        self : self

        RETURN
        ===========
        result : bool
            True if and only if the stack is empty

        EXAMPLE
        ===========
        >>> stack = myStack
        >>> stack.isEmpty()
        True
        """
        return not self.list

    def push(self, x):
        """
        Functions to push things to the stack

        PARAMETERS
        ===========
        self : self
        x :
            The value you want to push onto the stack

        EXAMPLE
        ===========
        stack = myStack()
        stack.push(5)
        """
        self.list.append(x)

    def pop(self):
        """
        Function to pop a value from the stack

        PARAMETERS
        ===========
        self : self

        RETURN 
        ===========
        top :
            the top value of the stack

        EXAMPLE
        ===========
        >>> stack = myStack()
        >>> stack.push(15)
        >>> stack.push(5)
        >>> stack.pop()
        5
        >>> stack.pop()
        15
        """
        if self.list:
            return self.list.pop()
        return None

    def peek(self):
        """
        Function to peek at the top variable on the stack

        PARAMETERS
        ===========
        self : self

        RETURN
        ===========
        top : 
            The value that is on the top of the stack
        
        EXAMPLE
        ===========
        >>> stack = myStack()
        >>> stack.push(15)
        >>> stack.push(5)
        >>> stack.peep()
        5
        >>> stack.peep()
        5
        """
        if not self.list:
            return None
        return self.list[-1]

