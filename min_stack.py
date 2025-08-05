class MinStack(object):

    def __init__(self):
        self.min_val = float('inf')
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.min_val = min(self.min_val, val)
        self.stack.append((val, self.min_val))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        if len(self.stack) == 0:
            self.min_val = float('inf')
        else:
            self.min_val = self.stack[-1][1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())