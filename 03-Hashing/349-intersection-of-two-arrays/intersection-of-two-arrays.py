class Solution(object):
    def intersection(self, nums1, nums2):
        result = []
        for left in range(0,len(nums1)):
            for right in range(0,len(nums2)):
                if nums1[left] == nums2[right]:
                    if nums1[left] not in result:
                        result.append(nums1[left])
        return result
                

        
        