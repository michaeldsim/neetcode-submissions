class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr = prices[0]

        for i in range(len(prices)):
            if i == 0:
                continue
            
            print(curr, prices[i])
            if curr > prices[i]:
                curr = prices[i]
            else:
                res = max(prices[i] - curr, res)
        
        return res