class Trie:

    def __init__(self):
        self.words_visited = set()
        self.prefix_visited = set()

    def insert(self, word: str) -> None:
        self.words_visited.add(word)
        for i in range(len(word)):
            self.prefix_visited.add(word[:i + 1])

    def search(self, word: str) -> bool:
        return word in self.words_visited

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefix_visited

if __name__=="__main__":
    # Example 1
    t = Trie()
    t.insert("apple")
    print(t.search("apple"))
    print(t.search("app"))
    print(t.startsWith("app"))
    t.insert("app")
    print(t.search("app"))