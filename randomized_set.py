class RandomizedSet:

    def __init__(self):
        self.hashmap = {}

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            del self.hashmap[val]
            return True
        return False

    def getRandom(self) -> int:
        import numpy as np
        indices = [i for i in range(len(self.hashmap))]
        keys = list(self.hashmap.keys())

        idx = np.random.choice(indices)
        return keys[idx]

if __name__=="__main__":
    # Example 1
    s = RandomizedSet()
    print(s.insert(1))
    print(s.remove(2))
    print(s.insert(2))
    print(s.getRandom())
    print(s.remove(1))
    print(s.insert(2))
    print(s.getRandom())