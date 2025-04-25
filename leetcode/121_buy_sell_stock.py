from typing import List
import math


class Solution:
    def maxProfit(self, prices:List[int])->int:
        if not prices:
            return 0

        min_price=prices[0]

        max_profit=0

        for price in prices[1:]:

            min_price=min(min_price,price)

            profit=price-min_price

            max_profit=max(max_profit,profit)


        return max_profit


sol=Solution()

print(sol.maxProfit([7,1,5,3,6,4]))

print(sol.maxProfit([7,6,4,3,1]))