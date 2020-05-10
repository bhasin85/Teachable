class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit_loss = []
        
        if len(prices) < 2:
            return max_profit
        
        for day in range(1, len(prices)):
            profit_loss.append(prices[day]-prices[day-1])
            
        prev = None
        for i in range(len(profit_loss)):
            if profit_loss[i]>0:
                max_profit += profit_loss[i]
        
        return max_profit
