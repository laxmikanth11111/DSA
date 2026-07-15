class Solution(object):
    def subsets(self, nums):
        result = []
        def backtrack(index, subsett):
            if index >= len(nums):
                result.append(subsett[:])
                return
            subsett.append(nums[index])
            backtrack(index + 1, subsett)
            subsett.pop()
            backtrack(index + 1, subsett)
        backtrack(0,[])
        return result
            
        
        