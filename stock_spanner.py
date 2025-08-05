class StockSpanner:

    def __init__(self):
        self.cur_idx = 0
        self.stack = []

    def next(self, price: int) -> int:
        if len(self.stack) == 0:
            self.stack.append((price, self.cur_idx))
            self.cur_idx += 1
            return 1
        # @print(self.stack)

        while len(self.stack) > 0 and self.stack[-1][0] <= price:
            cur_price, cur_idx = self.stack.pop()

        if len(self.stack) == 0:
            num_days = self.cur_idx + 1
        else:
            lower_price, lower_price_idx = self.stack[-1]
            num_days = self.cur_idx - lower_price_idx
        self.stack.append((price, self.cur_idx))

        self.cur_idx += 1

        return num_days

if __name__=="__main__":
    # Example 1
    s = StockSpanner()
    print(s.next(100))
    print(s.next(80))
    print(s.next(60))
    print(s.next(70))
    print(s.next(60))
    print(s.next(75))
    print(s.next(85))