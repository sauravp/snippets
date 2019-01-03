# https://www.interviewbit.com/problems/largest-rectangle-in-histogram/

class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        stack = [-1]
        maxArea = 0

        for i in range(len(A)):
            while stack[-1] != -1 and A[stack[-1]] >= A[i]:
                top_idx = stack.pop()
                maxArea = max(maxArea, A[top_idx] * (i - stack[-1] -1))
            stack.append(i)

        while stack[-1] != -1:
            top_idx = stack.pop()
            maxArea = max(maxArea, A[top_idx] * (len(A) - stack[-1] - 1))

        return maxArea
