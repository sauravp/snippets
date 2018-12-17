# https://www.interviewbit.com/problems/merge-two-sorted-lists-ii/

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        i, j = 0, 0
        while j < len(B):
            if B[j] < A[i]:
                A.insert(i, B[j])
                if i < len(A) - 1:
                    i += 1
                    j += 1
            elif i < len(A) - 1:
                    i += 1
            else:
                A.extend(B[j:])
                j = len(B)
        print( " ".join(map(str, A)) + " ")
