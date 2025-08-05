import heapq
from collections import defaultdict


def topKFrequent(words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """

    word_freq = defaultdict(int)

    for word in words:
        word_freq[word] += 1

    heap = []
    for word, freq in word_freq.items():
        heapq.heappush(heap, (-1 * freq, word))

    res = []
    for _ in range(k):
        res.append(heapq.heappop(heap)[1])

    return res

if __name__ == '__main__':
    # Example 1
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    print(topKFrequent(words, k))

    # Example 2
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    print(topKFrequent(words, k))