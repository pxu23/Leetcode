class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.circular_queue = [0] * k
        self.capacity = k
        self.num_elem = 0
        self.rear = -1
        self.front = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.num_elem == self.capacity:
            return False

        self.circular_queue[(self.rear + 1) % self.capacity] = value
        self.num_elem += 1
        self.rear += 1
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.num_elem == 0:
            return False
        self.front += 1
        self.num_elem -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.num_elem == 0:
            return -1
        return self.circular_queue[self.front % self.capacity]

    def Rear(self):
        """
        :rtype: int
        """
        if self.num_elem == 0:
            return -1
        return self.circular_queue[self.rear % self.capacity]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.num_elem == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.num_elem == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
print(obj.enQueue(1))
print(obj.enQueue(2))
print(obj.enQueue(3))
print(obj.Rear())
print(obj.isFull())
print(obj.deQueue())
print(obj.enQueue(4))
print(obj.Rear())