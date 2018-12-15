# https://www.interviewbit.com/problems/prettyprint/

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        cache = {}
        center = A - 1
        for i in range(2*A - 1):
            for j in range(2*A - 1):
                cache[(i, j)] = max(abs(i-center), abs(j-center)) + 1
                
        answer = []
        for i in range(2*A - 1):
            answer.append([cache[(i, j)] for j in range(2*A - 1)])
        return answer
