class Solution(object):
    def moveZeroes(self, nums):
        left = 0
        for value in range(len(nums)):
            if nums[value] != 0:
                nums[value], nums[left] = nums[left], nums[value]
                left += 1
        return nums
        


        