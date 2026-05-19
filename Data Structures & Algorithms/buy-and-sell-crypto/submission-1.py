class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxp=0
        i,j=0,1

        while j<len(prices):

            if(prices[i]<prices[j]):
                prof=prices[j]-prices[i]
                maxp=max(maxp,prof)
            
            else:
                i=j
            j=j+1
        
        return maxp

            
        