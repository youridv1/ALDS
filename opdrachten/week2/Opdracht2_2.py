from Opdracht2_1 import myStack

def bracketsProblem(s: str):
    """
    Function to check if the bracket syntax of a given string is correct

    PARAMETERS
    ===========
    s : str

    RETURN
    ===========
    result : bool
        True if and only if there are no loose brackets in the given string

    EXAMPLE
    ===========
    >>> string = "{[()]}"
    >>> bracketsProblem(string)
    True
    >>> string = "{[(]}"
    >>> bracketsProblem(string)
    False
    """
    open = '<{(['
    close = '>})]'
    stack = myStack()
    for char in s:
        if char in open:
            stack.push(char)
        elif char in close and open[close.find(char)] == stack.peek():
            stack.pop()
        elif char in close:
            return False
    return stack.isEmpty()

string = "[{()}]"
print(bracketsProblem(string))