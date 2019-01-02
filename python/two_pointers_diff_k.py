# https://www.interviewbit.com/problems/diffk/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        if len(A) <= 1:
            return 0
        
        i = 0
        j = 0
        while i < len(A) and j < len(A):
            if A[i] - A[j] == B and i != j:
                return 1
            elif A[i] - A[j] < B:
                i += 1
            else:
                j += 1
        return 0
