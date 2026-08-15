class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxi=prices[0]
        answer=0
        for i in range(1,len(prices)):
            if prices[i]>maxi or prices[i]<mini:
                maxi=prices[i]
            if prices[i-1]<mini or prices[i-1]>maxi:
                mini=prices[i-1]
            if mini<maxi:
                answer=max(answer,maxi-mini)
        return answer