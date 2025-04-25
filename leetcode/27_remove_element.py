from typing import List

class Solution:
    def removeElement(self, nums:List[int], val:int)->int:
        k=0

        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]

                k+=1

        return k

sol=Solution()

nums1=[3,2,2,3]
val1=3
k1=sol.removeElement(nums1,val1)
print(f"K1= {k1}, nums1={nums1[:k1]}")

nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
k2 = sol.removeElement(nums2, val2)
print(f"k2={k2}, nums2={nums2[:k2]}")