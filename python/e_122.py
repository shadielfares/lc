class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0

        while l < len(prices)-1:
            #Note it doesn't go out of range
            r = l + 1
            #Determine if right is smaller than left
            if prices[r] > prices[l]:
                profit += prices[r] - prices[l]
                print(prices[l], prices[r])
                print(l, r)
                print(profit)

            l += 1
        return profit

    #1: Profit = 1
    #2: Profit = 2
    #---------
    # Profit = 4
    #