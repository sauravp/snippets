# https://www.interviewbit.com/problems/grid-unique-paths/

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def __init__(self):
        self.cache = {}
        
    def uniquePaths(self, A, B):
        if A == 0 or B == 0:
            self.cache[(0, 0)] = 0
            return 0
        if A == 1 or B == 1:
            for i in range(A):
                self.cache[(i, 1)] = 1
            for j in range(B):
                self.cache[(1, j)] = 1
            return 1
        if (A, B-1) not in self.cache:
            self.cache[(A, B-1)] = self.uniquePaths(A, B-1)
        if (A-1, B) not in self.cache:
            self.cache[(A-1, B)] = self.uniquePaths(A-1, B)
        return  self.cache[(A, B-1)] + self.cache[(A-1, B)]
