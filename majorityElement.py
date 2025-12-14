#The majority element is the element that appears more than ⌊n / 2⌋ times. 
#You may assume that the majority element always exists in the array.


class Solution:

    def findMajorityElement(self, nums: List[]) -> int:

         sorted_list = sorted(nums)
         
         return  sorted_list(len(nums) // 2)
         


  