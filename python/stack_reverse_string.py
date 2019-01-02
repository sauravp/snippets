# https://www.interviewbit.com/problems/reverse-string/

class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        chars = list(A)
        stack = []
        for char in chars:
            stack.append(char)
        
        outstr = ""
        while len(stack) > 0:
            outstr += stack.pop()
        
        return outstr
