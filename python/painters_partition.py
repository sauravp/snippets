# https://www.interviewbit.com/problems/painters-partition-problem/

from sys import maxint 

class Solution:
    # @param A : integer (number of painters)
    # @param B : integer (time to paint 1 unit)
    # @param C : list of integers (boards)
    # @return an integer
    def paint(self, A, B, C):
        return B * self.partition(A, C) % 10000003

    
    def partition(self, A, C):
        n = len(C)
         # base cases 
        if A == 1: # one partition 
            return sum(C)
        if n == 1: # one board 
            return C[0] 
        best = maxint
 
        for i in range(1, n): 
            best = min(best, max(self.partition(A - 1,  C[:i]), sum(C[i:])))
        return best
