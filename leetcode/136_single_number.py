from typing import List


class Solution:
    def singleNumber_xor(self, nums: List[int]) -> int:
        # Most efficient space-wise
        result = 0
        for num in nums:
            result ^= num
        return result
    

sol = Solution()
data = [4,1,2,1,2]
print(f"XOR: {sol.singleNumber_xor(data)}") 