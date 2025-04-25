from typing import List

class Solution:
    def removeDuplicates(self,nums: List[int]) -> int:
        if not nums:
            return 0

        k=1
        for i in range(1, len(nums)):
            if(nums[i]!=nums[i-1]):
                nums[k]=nums[i]

                k+=1

        return k


sol=Solution()

nums1=[1,1,2]

k1=sol.removeDuplicates(nums1)

print(f"k1={k1}, nums1={nums1[:k1]}")

nums2=[0,0,1,1,1,2,2,3,3,4]
k2=sol.removeDuplicates(nums2)

print(f"k2= {k2}, nums2= {nums2[:k2]}")

