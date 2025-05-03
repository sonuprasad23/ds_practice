from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(acc) for acc in accounts) if accounts else 0


sol = Solution()
print(sol.maximumWealth([[2,8,7], [7,1,3], [1,9,5]])) 
