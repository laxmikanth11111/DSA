class Solution(object):
    def lengthOfLongestSubstring(self, s):
        my_dict = {}
        right = 0
        left = 0
        maxi = 0
        while right < len(s):
            if s[right] in my_dict:
                left = max(left,my_dict[s[right]]+1)
            maxi = max(maxi, right - left + 1)
            my_dict[s[right]] = right
            right += 1
        return maxi
            

        