# https://www.interviewbit.com/problems/add-one-to-number

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        carry = False
        stop = False
        i = len(A) - 1
        while not stop and i >= 0:
            if A[i] == 9:
                A[i] = 0
                carry = True
            else:
                A[i] += 1
                carry = False
                stop = True
            i -= 1
        if i==-1 and carry:
            A = [1] + A
        return self._strip(A)
    
    def _strip(self, A):
        i = 0
        n = len(A)
        B = A
        while i < n and B[i] == 0:
            B = B[1:]
        return B
