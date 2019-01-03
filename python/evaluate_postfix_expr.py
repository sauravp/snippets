# https://www.interviewbit.com/problems/evaluate-expression/

import operator

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        ops = {"+": operator.add,
               "-": operator.sub,
               "*": operator.mul,
               "/": operator.floordiv
               }
        stack = []
        
        for entry in A:
            if entry not in ops:
                stack.append(int(entry))
            else:
                oprnd2 = stack.pop()
                oprnd1 = stack.pop()
                stack.append(ops[entry](oprnd1, oprnd2))
        
        if len(stack) != 1:
            return 0
        else:
            return stack[0]
