# https://www.interviewbit.com/problems/sort-by-color/

class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        counts = [0, 0, 0]
        
        for item in A:
            counts[item] += 1
        
        for idx in range(len(A)):
            if idx < counts[0]:
                A[idx] = 0
            elif idx < counts[0] + counts[1]:
                A[idx] = 1
            else:
                A[idx] = 2
        
        return A
