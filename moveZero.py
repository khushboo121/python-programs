#move all 0's to the end of it while maintaining the relative order of the non-zero elements.

class Solution:

    def moveZeros(self, nums: List[int]) -> None:

        step = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[step],nums[i] = nums[i],nums[step]
                step += 1


if __name__ == '__main__':

    nums = [1,0,0,1,2,0,3]
    object1 = Solution()
    object1.moveZeros(nums)
    print(f'nums:', nums)
