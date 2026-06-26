class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b,s=0,1
        profit=0
        maxP=0
        while s<len(prices):
            if prices[s]>prices[b]:
                profit=prices[s]-prices[b]
                s+=1
                maxP=max(maxP,profit)
            else:
                b=s
                s+=1
        return maxP