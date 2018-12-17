# https://www.interviewbit.com/problems/square-root-of-integer/

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        start, end = 1, A

        while start <= end :
            mid = (start + end) / 2
            # we found exact sqrt
            if mid * mid == A :
                return mid
            # go on right side
            elif mid * mid < A :
                start = mid + 1
            # go on left side
            else :
                end = mid - 1;
        # perfect sqrt not found, return floor
        return start-1
