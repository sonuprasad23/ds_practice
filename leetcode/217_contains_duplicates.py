from typing import List

class Solution:
    def containsDuplicate_set(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    def containsDuplicate_sort(self, nums: List[int]) -> bool:
        nums.sort() # Sorts in-place
        for i in range(len(nums) - 1): # Iterate up to second-to-last element
            if nums[i] == nums[i+1]:
                return True
        return False

    def containsDuplicate_oneliner(self, nums: List[int]) -> bool:
        # Clever approach: compare length of list to length of set derived from list
        return len(nums) != len(set(nums))


# Example Usage
sol = Solution()
print(f"Set Approach: {sol.containsDuplicate_set([1,2,3,1])}")      # True
print(f"Sort Approach: {sol.containsDuplicate_sort([1,2,3,1])}")     # True
print(f"One-liner Approach: {sol.containsDuplicate_oneliner([1,2,3,1])}") # True

print(f"Set Approach: {sol.containsDuplicate_set([1,2,3,4])}")      # False
print(f"Sort Approach: {sol.containsDuplicate_sort([1,2,3,4])}")     # False
print(f"One-liner Approach: {sol.containsDuplicate_oneliner([1,2,3,4])}") # False