class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Index of largest value that is greater than the lowest value'
        lowest_value = math.inf
        max_profit = 0
        for price in prices:
            if price < lowest_value:
                lowest_value = price
            else:
                #Calculate profit
                max_profit = max(max_profit, price - lowest_value)
        
        return max_profit