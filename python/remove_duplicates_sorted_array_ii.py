# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        current = None
        run = 0
        i = 0
        while i < len(A):
            if A[i] != current:
                current = A[i]
                i += 1
                run = 1
            elif run < 2:
                i += 1
                run += 1
            else:
                del A[i]
            
        return len(A)
