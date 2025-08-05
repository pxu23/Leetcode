class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.removed_element = set()

    def popSmallest(self) -> int:
        popped = self.smallest
        self.removed_element.add(popped)
        n = len(self.removed_element)

        for i in range(popped + 1, popped + 1 + n):
            if i not in self.removed_element:
                self.smallest = i
                break
        return popped

    def addBack(self, num: int) -> None:
        if num in self.removed_element:
            self.removed_element.remove(num)
            self.smallest = min(self.smallest, num)

if __name__=="__main__":
    # Example 1
    s = SmallestInfiniteSet()
    s.addBack(2)
    print(s.popSmallest())
    print(s.popSmallest())
    print(s.popSmallest())
    s.addBack(1)
    print(s.popSmallest())
    print(s.popSmallest())
    print(s.popSmallest())