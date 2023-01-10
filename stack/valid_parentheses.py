def isValid(s):
        '''
        Valid chars '(',')','{','}','[',']'
        Open and close brackets by same type and correct order.
        Every bracket has its corresponding char

        If its odd by default is invalid

        Next, we will loop the string and push the corresponding closing char
        of the valid char whenever is an opening char.
        When is a closing one we will check first if there are values in the
        stack, which if there is not, it means that we are looking at a closing
        char that didn't had an opening char.
        We will also validate that the closing char corresponds to the one we are
        looping, that's why we added the correspending closing, because it forces
        a validation for the correct order.
        '''
        if len(s)%2 != 0:
            return False

        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            elif not stack or char != stack.pop():
                return False
                
        return not stack

if __name__ == "__main__":
    assert True == isValid("()")
    assert False == isValid("(]")
    assert True == isValid("()[]{}")
    assert False == isValid("({([(]))})([)]")
    assert False == isValid("){")
    