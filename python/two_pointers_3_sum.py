# https://www.interviewbit.com/problems/3-sum/

import sys

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        closest_sum = sys.maxsize
        
        for i in range(len(A)):
            if i!=len(A)-1:
                temp = A[:i] + A[i+1:]
            else:
                temp = A[:len(A)-1]
            temp = sorted(temp)
            
            l, r = 0, len(temp) - 1
            diff = B - A[i]
            
            while l < r:
                if abs(temp[l] + temp[r] + A[i] - B) < abs(closest_sum - B):
                    closest_sum = temp[l] + temp[r] + A[i]
                
                if temp[l] + temp[r] + A[i] == B:
                    return B
                elif temp[l] + temp[r] + A[i] > B:
                    r = r - 1
                else:
                    l = l + 1
                    
        return closest_sum
