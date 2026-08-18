class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        my_profit = 0
        minSel = prices[0]
        index_min = 0

        for i,profit in enumerate(prices):
            if(minSel > profit and index_min < i):
                minSel = profit
                index_min = i
            
            if(minSel < profit and my_profit < (profit - minSel)):
                    my_profit = profit - minSel
        
        return my_profit
