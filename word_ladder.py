from collections import deque

def ladderLength(beginWord, endWord, wordList):
    wordSet = set(wordList)
    queue = deque()
    queue.append(beginWord)
    visited = set()
    visited.add(beginWord)

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    min_moves = 1
    while queue:
        n = len(queue)
        for _ in range(n):
            cur_word = queue.popleft()
            if cur_word == endWord:
                return min_moves

            for i in range(len(cur_word)):
                first_part = cur_word[:i]
                next_part = cur_word[i + 1:]
                for let in letters:
                    new_word = first_part + let + next_part
                    if new_word in wordSet:
                        if new_word in visited:
                            continue
                        queue.append(new_word)
                        visited.add(new_word)
        min_moves += 1

    return 0

if __name__=="__main__":
    # Example 1
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(ladderLength(beginWord, endWord, wordList))

    # Example 2
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    print(ladderLength(beginWord, endWord, wordList))