from typing import List

class Solution:
    def twoSum_hashmap(self,nums:List[int], target:int) ->List[int]:
        seen_map={}

        for i, num in enumerate(nums):
            complement=target-num

            if complement in seen_map:
                return [seen_map[complement],i]

            seen_map[num]=id

        return []


    def twoSum_brute_force(self,nums:List[int], target:int)->List[int]:
        n=len(nums)

        for i in range(n):
            for j in range(i+1,n):
                if(nums[i]+nums[j]==target):
                    return [i,j]

        return []




sol=Solution()

print(f"Hashmap: {sol.twoSum_hashmap([2,7,11,15],9)}")

print(f"Brute Force : {sol.twoSum_brute_force([2,7,11,15],9)}")

print(f"Hashmap: {sol.twoSum_hashmap([3, 2, 4], 6)}") # Output: [1, 2]
print(f"Brute Force: {sol.twoSum_brute_force([3, 3], 6)}") # Output: [0, 1]