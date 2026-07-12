class Solution(object):
    def isPerfectSquare(self, num):
        low = 1
        high = num
        while low <= high:
            mid = (low + high)//2
            result = mid * mid
            if result == num:
                return True
            elif result < num:
                low = mid + 1
            else:
                high = mid - 1
        return False

            
           
            
        