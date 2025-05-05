from typing import List

class Solution:
    def sortedSquares_simple(self, nums:List[int]) -> List[int]:
        squares = [x*x for x in nums]
        squares.sort()
        return squares
    
     def sortedSquares_two_pointers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n # Pre-allocate result list
        left, right = 0, n - 1
        # Fill result from right to left (index k)
        k = n - 1
        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2
            if left_sq > right_sq:
                result[k] = left_sq
                left += 1
            else:
                result[k] = right_sq
                right -= 1
            k -= 1 # Move fill position to the left
        return result
