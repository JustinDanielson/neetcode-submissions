class Solution:
    '''
    You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
    You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
    Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
    '''
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