class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Transaction = namedtuple("Transaction", ["price", "day"])
        buy = None
        max_profit = 0
        for day, price in enumerate(prices):
            if not buy or buy.price > price:
                buy = Transaction(price, day)
            elif buy.price < price and max_profit < price - buy.price:
                max_profit = price - buy.price
                sell = Transaction
        return max_profit