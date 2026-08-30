class Solution(object):
    def mySqrt(self, x):
        low = 1
        high = x
        ans = 0 
        while low <= high:
            mid = (low + high)//2 
            result = mid * mid
            if result == x :
                return mid
            elif result < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

        