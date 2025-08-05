class WordDictionary:

    def __init__(self):
        self.visited_word = set()

    def addWord(self, word: str) -> None:
        self.visited_word.add(word)

    def search(self, word: str) -> bool:
        def checkSameForm(word1, word2):
            if len(word1) != len(word2):
                return False

            for i in range(len(word1)):
                if word1[i] == ".":
                    continue
                if word2[i] != word1[i]:
                    return False
            return True

        if "." not in word:
            return word in self.visited_word
        else:
            for word2 in self.visited_word:
                if checkSameForm(word, word2):
                    return True
            return False

if __name__=="__main__":
    # Example 1
    d = WordDictionary()
    d.addWord("bad")
    d.addWord("mad")
    d.addWord("dad")
    print(d.search("pad"))
    print(d.search("bad"))
    print(d.search(".ad"))
    print(d.search("b.."))