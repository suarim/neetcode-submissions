class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        minprice=999999
        for i in prices:
            minprice = min(minprice,i)
            maxprofit = max(maxprofit,i-minprice)
        return maxprofit
        