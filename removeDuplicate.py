
#
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
               nums[k] = nums[i]
               k += 1

        return k


if __name__ == '__main__':
     nums = [0,0,1,2,2,2,3,3,4,5,5] 
     object1 = Solution()     
     count = object1.removeDuplicates(nums)
     print(f'count:', count) # count the unique elements
     print(f'nums:',nums)  

     #expect put nums=[0,1,2,3,4,5,....]
           

