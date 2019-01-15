# https://www.interviewbit.com/problems/search-for-a-range/

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        first_idx = self.searchFirst(A, B)
        last_idx = self.searchLast(A, B)
        
        return [first_idx, last_idx]
        
    
    def searchFirst(self, A, B):
        start, end, result = 0, len(A) - 1, -1
        
        while start <= end:
            mid = (start + end) / 2
            if A[mid] == B:
                result = mid
                end = mid - 1
            elif A[mid] > B:
                end = mid - 1
            else:
                start = mid + 1
        
        return result
    
    def searchLast(self, A, B):
        start, end, result = 0, len(A) - 1, -1
        
        while start <= end:
            mid = (start + end) / 2
            if A[mid] == B:
                result = mid
                start = mid + 1
            elif A[mid] > B:
                end = mid - 1
            else:
                start = mid + 1
        
        return result
            
                
