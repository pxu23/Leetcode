from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.recent_requests = 0
        self.queue = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)

        while self.queue[0] < t - 3000:
            elem = self.queue.popleft()
            self.recent_requests -= 1

        self.recent_requests += 1
        return self.recent_requests

if __name__=="__main__":
    # Example 1
    recentCounter = RecentCounter()
    print(recentCounter.ping(1))
    print(recentCounter.ping(100))
    print(recentCounter.ping(3001))
    print(recentCounter.ping(3002))