# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        current = None
        output = 0
        i = 0
        while i < len(A):
            if A[i] != current:
                current = A[i]
                output += 1
                i += 1
            else:
                del A[i]
        return output
